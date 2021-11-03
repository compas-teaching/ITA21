import compas
from compas.artists import Artist

mesh = compas.json_load('tubemesh.json')

Artist.clear()

artist = Artist(mesh)

artist.draw_vertices()
artist.draw_edges()
# artist.draw_faces()

Artist.redraw()
