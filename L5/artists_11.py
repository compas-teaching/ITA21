import compas
from compas.artists import Artist

mesh = compas.json_load('tubemesh.json')

mesh.flip_cycles()

Artist.clear()

artist = Artist(mesh)

faces = mesh.face_sample(size=50)

artist.draw_vertices()
artist.draw_edges()
artist.draw_faces(faces=faces)

Artist.redraw()
