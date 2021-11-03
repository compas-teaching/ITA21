import compas
from compas.artists import Artist

mesh = compas.json_load('tubemesh.json')

mesh.flip_cycles()

Artist.clear()

artist = Artist(mesh)

artist.draw_vertices()
artist.draw_faces()
artist.draw_vertexlabels()

Artist.redraw()
