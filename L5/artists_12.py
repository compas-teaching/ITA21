import random
import compas
from compas.artists import Artist
from compas.utilities import i_to_rgb

mesh = compas.json_load('tubemesh.json')

mesh.flip_cycles()

Artist.clear()

artist = Artist(mesh)

color = {
    face: i_to_rgb(random.random(), normalize=False)
    for face in mesh.faces()
}

artist.draw_vertices()
artist.draw_faces(color=color)

Artist.redraw()
