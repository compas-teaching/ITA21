import os
import random
import compas
from compas.artists import Artist
from compas.utilities import i_to_rgb

here = os.path.dirname(__file__)
path = os.path.join(here, 'tubemesh.json')

mesh = compas.json_load(path)
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
