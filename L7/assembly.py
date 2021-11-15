from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from collections import deque

from compas.datastructures import Datastructure
from compas.datastructures import Graph
from compas.datastructures import Mesh

from compas.geometry import Frame
from compas.geometry import Polyhedron as Shape
from compas.geometry import Transformation
from compas.geometry import boolean_union_mesh_mesh
from compas.geometry import boolean_difference_mesh_mesh
from compas.geometry import boolean_intersection_mesh_mesh


class Assembly(Datastructure):
    """A data structure for managing the connections between different parts of an assembly.
    Attributes
    ----------
    attributes: dict
        General attributes of the assembly that will be included in the data dict.
    graph: :class:`compas.datastructures.Graph`
        The graph that is used under the hood to store the parts and their connections.
    """

    @property
    def DATASCHEMA(self):
        import schema
        return schema.Schema({
            "attributes": dict,
            "graph": Graph,
        })

    @property
    def JSONSCHEMANAME(self):
        return 'assembly'

    def __init__(self, name=None, **kwargs):
        super(Assembly, self).__init__()
        self.attributes = {}
        self.graph = Graph()
        self._parts = {}
        if kwargs:
            self.attributes.update(kwargs)

    def __str__(self):
        tpl = "<Assembly with {} parts and {} connections>"
        return tpl.format(self.graph.number_of_nodes(), self.graph.number_of_edges())

    @property
    def data(self):
        """dict : A data dict representing the assembly data structure for serialization.
        """
        data = {
            'attributes': self.attributes,
            'graph': self.graph.data,
        }
        return data

    @data.setter
    def data(self, data):
        self.attributes.update(data['attributes'] or {})
        self.graph.data = data['graph']

    def add_part(self, part, key=None, **kwargs):
        """Add a part to the assembly.
        Parameters
        ----------
        part: :class:`compas.datastructures.Part`
            The part to add.
        key: int or str, optional
            The identifier of the part in the assembly.
            Note that the key is unique only in the context of the current assembly.
            Nested assemblies may have the same ``key`` value for one of their parts.
            Default is ``None`` in which case the key will be automatically assigned integer value.
        kwargs: dict
            Additional named parameters collected in a dict.
        Returns
        -------
        int or str
            The identifier of the part in the current assembly graph.
        """
        key = self.graph.add_node(key=key, part=part, **kwargs)
        part.key = key
        self._parts[part.guid] = part
        return key

    def add_connection(self, a, b, **kwargs):
        """Add a connection between two parts.
        Parameters
        ----------
        a: :class:`compas.datastructures.Part`
            The "from" part.
        b: :class:`compas.datastructures.Part`
            The "to" part.
        kwargs: dict
            Additional named parameters collected in a dict.
        Returns
        -------
        tuple of str or int
            The tuple of node identifiers that identifies the connection.
        Raises
        ------
        :class:`AssemblyError`
            If ``a`` and/or ``b`` are not in the assembly.
        """
        if a.key is None or b.key is None:
            raise Exception('Both parts have to be added to the assembly before a connection can be created.')
        if not self.graph.has_node(a.key) or not self.graph.has_node(b.key):
            raise Exception('Both parts have to be added to the assembly before a connection can be created.')
        return self.graph.add_edge(a.key, b.key, **kwargs)

    def parts(self):
        """The parts of the assembly.
        Yields
        ------
        :class:`compas.datastructures.Part`
            The individual parts of the assembly.
        """
        for node in self.graph.nodes():
            yield self.graph.node_attribute(node, 'part')

    def connections(self):
        """The connections between the parts."""
        return self.graph.edges()

    def find(self, guid):
        """Find a part in the assembly by its GUID.
        Parameters
        ----------
        guid: str
            A globally unique identifier.
            This identifier is automatically assigned when parts are created.
        Returns
        -------
        :class:`compas.datastructures.Part` or None
            The identified part, if any.
        """
        return self._parts.get(guid)


class Part(Datastructure):
    """A data structure for representing assembly parts.
    Parameters
    ----------
    name : str, optional
        The name of the part.
        The name will be stored in :attr:`Part.attributes`.
    frame : :class:`compas.geometry.Frame`, optional
        The local coordinate system of the part.
    shape : :class:`compas.geometry.Shape`, optional
        The base shape of the part geometry.
    features : list of tuple(:class:`compas.geometry.Shape`, str), optional
        The features to be added to the base shape of the part geometry.
    Attributes
    ----------
    attributes : dict
        General object attributes that will be included in the data dict.
    key : int or str
        The identifier of the part in the connectivity graph of the parent assembly.
    frame : :class:`compas.geometry.Frame`
        The local coordinate system of the part.
    shape : :class:`compas.geometry.Shape`
        The base shape of the part geometry.
    features : list of tuple(:class:`compas.geometry.Shape`, str)
        The features added to the base shape of the part geometry.
    transformations : deque of :class:`compas.geometry.Transformation`
        The stack of transformations applied to the part geometry.
        The most recent transformation is on the left of the stack.
        All transformations are with respect to the local coordinate system.
    """

    operations = {
        'union': boolean_union_mesh_mesh,
        'difference': boolean_difference_mesh_mesh,
        'intersection': boolean_intersection_mesh_mesh
    }

    @property
    def DATASCHEMA(self):
        import schema
        return schema.Schema({
            "attributes": dict,
            "key": int,
            "frame": Frame,
            "shape": Shape,
            "features": list,
            "transformations": list,
        })

    @property
    def JSONSCHEMANAME(self):
        return 'part'

    def __init__(self, name, frame=None, shape=None, features=None, **kwargs):
        super(Part, self).__init__()
        self._frame = None
        self.attributes = {'name': name or 'Part'}
        self.key = None
        self.frame = frame
        self.shape = shape or Shape([], [])
        self.features = features or []
        self.transformations = deque()
        if kwargs:
            self.attributes.update(kwargs)

    def __str__(self):
        tpl = "<Part with shape {} and features {}>"
        return tpl.format(self.shape, self.features)

    @property
    def data(self):
        """dict : A data dict representing the part attributes, the assembly graph identifier, the local coordinate system,
        the base shape, the shape features, and the transformation tack wrt to the local coordinate system.
        """
        data = {
            'attributes': self.attributes,
            "key": self.key,
            "frame": self.frame.data,
            "shape": self.shape.data,
            "features": [(shape.data, operation) for shape, operation in self.features],
            "transformations": [T.data for T in self.transformations],
        }
        return data

    @data.setter
    def data(self, data):
        self.attributes.update(data['attributes'] or {})
        self.key = data['key']
        self.frame.data = data['frame']
        self.shape.data = data['shape']
        self.features = [(Shape.from_data(shape), operation) for shape, operation in data['features']]
        self.transformations = deque([Transformation.from_data(T) for T in data['transformations']])

    @property
    def frame(self):
        if not self._frame:
            self._frame = Frame.worldXY()
        return self._frame

    @frame.setter
    def frame(self, frame):
        self._frame = frame

    @property
    def geometry(self):
        # this is a temp solution
        if self.features:
            A = Mesh.from_shape(self.shape)
            for shape, operation in self.features:
                A.quads_to_triangles()
                B = Mesh.from_shape(shape)
                B.quads_to_triangles()
                A = Part.operations[operation](A.to_vertices_and_faces(), B.to_vertices_and_faces())
            geometry = Shape(*A)
        else:
            geometry = self.shape.copy()
        T = Transformation.from_frame_to_frame(Frame.worldXY(), self.frame)
        geometry.transform(T)
        return geometry

    def transform(self, T):
        """Transform the part with respect to the local cooordinate system.
        Parameters
        ----------
        T : :class:`compas.geometry.Transformation`
        """
        self.transformations.appendleft(T)
        self.shape.transform(T)
        for shape, operation in self.features:
            shape.transform(T)

    def add_feature(self, shape, operation):
        """Add a feature to the shape of the part and the operation through which it should be integrated.
        Parameters
        ----------
        shape : :class:`compas.geometry.Shape`
            The shape of the feature.
        operation : {'union', 'difference', 'intersection'}
            The boolean operation through which the feature should be integrated in the base shape.
        """
        if operation not in Part.operations:
            raise Exception
        self.features.append((shape, operation))

    # def apply_transformations(self):
    #     """Apply all transformations to the part shape."""
    #     X = Transformation.from_frame(self.frame)
    #     transformations = self.transformations[:]
    #     transformations.append(X)
    #     T = reduce(multiply_matrices, transformations)
    #     self.shape.transform(T)

    def to_mesh(self, cls=None):
        """Convert the part geometry to a mesh.
        Parameters
        ----------
        cls : :class:`compas.datastructures.Mesh`, optional
            The type of mesh to be used for the conversion.
        Returns
        -------
        :class:`compas.datastructures.Mesh`
            The resulting mesh.
        """
        cls = cls or Mesh
        return cls.from_shape(self.geometry)
