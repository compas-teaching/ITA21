import compas
from compas_rhino.artists import MeshArtist
from compas_rhino.artists import BoxArtist

mesh, box = compas.json_load('monkey-in-box.json')

artist = MeshArtist(mesh)
artist.draw_mesh()

artist = BoxArtist(mesh)
artist.draw_mesh()
