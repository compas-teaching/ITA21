import os
import compas
from compas.artists import Artist

here = os.path.dirname(__file__)
path = os.path.join(here, 'tubemesh.json')

mesh = compas.json_load(path)

mesh.flip_cycles()

Artist.clear()

artist = Artist(mesh)

faces = mesh.face_sample(size=50)

artist.draw_vertices()
artist.draw_edges()
artist.draw_faces(faces=faces)

Artist.redraw()
