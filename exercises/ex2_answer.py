import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

# deserialization the hexagon mesh
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'data', 'hexagon.json')
mesh = Mesh.from_json(FILE)

# choose a random edge sample from the mesh
start = mesh.edge_sample()[0]

# find edge strips
# ===================================================================================
# Modify the edge_strip(mesh, edge) algorithm for general n-gon meshes,
# which currently work for quad meshes.
# The algorithm should stop when n-gon with an odd number of sides is encountered.


def edge_strip(mesh, edge):
    """Find all edges on the same strip as a given edge.

    Parameters
    ----------
    edge : tuple of int
        The identifier of the starting edge.

    Returns
    -------
    list of tuple of int
        The edges on the same strip as the given edge.
    """
    edges = []
    v, u = edge
    while True:
        edges.append((u, v))
        face = mesh.halfedge[u][v]
        print(face, u, v)
        if face is None:
            break
        vertices = mesh.face_vertices(face)
        if len(vertices) % 2 != 0:
            break
        i = vertices.index(u)
        u = vertices[i - int(len(vertices) / 2) + 1]
        v = vertices[i - int(len(vertices) / 2)]

    edges[:] = [(u, v) for v, u in edges[::-1]]

    u, v = edge
    while True:
        face = mesh.halfedge[u][v]
        if face is None:
            break
        vertices = mesh.face_vertices(face)
        if len(vertices) % 2 != 0:
            break
        i = vertices.index(u)
        u = vertices[i - int(len(vertices) / 2) + 1]
        v = vertices[i - int(len(vertices) / 2)]
        edges.append((u, v))
    return edges


# ===================================================================================
# find edge strips
edges = edge_strip(mesh, start)

# find strip faces
faces = []
for u, v in edges:
    if mesh.halfedge_face(u, v) is not None:
        faces.append(mesh.halfedge_face(u, v))

# visualization edge settings
edgecolor = {}
edgewidth = {}
for (u, v) in edges:
    edgecolor[(u, v)] = (0, 1, 0)
    edgewidth[(u, v)] = 2.0
    edgecolor[(v, u)] = (0, 1, 0)
    edgewidth[(v, u)] = 2.0
edgecolor[start] = (1, 0, 0)

# visualization face settings
facecolor = {}
for face in faces:
    facecolor[face] = (1, 0.7, 0.7)

# plotter
plotter = Plotter()
artist = plotter.add(mesh,
                     facecolor=facecolor,
                     edgecolor=edgecolor,
                     edgewidth=edgewidth,
                     )

plotter.zoom_extents()
plotter.show()
