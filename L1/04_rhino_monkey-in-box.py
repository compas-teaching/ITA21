import compas
import compas_rhino
from compas_rhino.artists import MeshArtist
from compas_rhino.artists import BoxArtist

# clear the objects in the Rhino scene
compas_rhino.clear()

# load the mesh and box data
mesh, box = compas.json_load('/Users/vanmelet/Code/ITA21/monkey-in-box.json')

# viz the mesh
artist = MeshArtist(mesh)
artist.draw_mesh()

# viz the box
artist = BoxArtist(box)
artist.draw()
