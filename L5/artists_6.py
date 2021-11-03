import os
import compas
from compas.artists import Artist

here = os.path.dirname(__file__)
path = os.path.join(here, 'tubemesh.json')

mesh = compas.json_load(path)

Artist.clear()

artist = Artist(mesh)

artist.draw_vertices()
artist.draw_edges()
# artist.draw_faces()

Artist.redraw()
