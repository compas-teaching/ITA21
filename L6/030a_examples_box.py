import compas_rhino
from compas_rhino.geometry import RhinoBox
from compas.artists import Artist
from compas.geometry import Point, Vector
from compas.datastructures import Mesh
from compas.numerical import dr

# ==============================================================================
# Mesh from Box
# ==============================================================================

guid = compas_rhino.select_object('Select a box.')
box = RhinoBox.from_guid(guid).to_compas()
mesh = Mesh.from_shape(box)

# ==============================================================================
# Attributes
# ==============================================================================

# ==============================================================================
# DR
# ==============================================================================

# ==============================================================================
# Viz
# ==============================================================================

artist = Artist(mesh, layer="ITA21::L6::FormFinding")

vertexcolor = {vertex: (255, 0, 0) for vertex in mesh.vertices_where({'is_anchor': True})}

artist.clear_layer()
artist.draw(vertexcolor=vertexcolor)

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()