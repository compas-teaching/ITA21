import compas
from compas.artists import Artist

mesh = compas.json_load('tubemesh.json')

Artist.clear()

artist = Artist(mesh)

artist.draw_mesh(disjoint=True)

Artist.redraw()
