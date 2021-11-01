from compas.datastructures import Mesh
from compas_plotters import Plotter

# generate a mesh grid from meshgrid
mesh = Mesh.from_meshgrid(nx=5, dx=2)

# choose a random face sample from the mesh
start = mesh.face_sample()[0]

# develop checkered pattern starting from the start face
# checkered pattern contains two colors where a single checker is surrounded
# on all four sides by a checker of a different color.

# Hint1: you can use face attribute to store the color information. e.g. "is_colored": True / False
# To should avoid an infitie loop, you should find a way to check the face and its neighbours only once

# Hint2: Mesh.face_neighbors, Mesh.update_default_face_attribute, Mesh.face_attribute

mesh.update_default_face_attributes({'is_colored': None})
mesh.face_attribute(start, 'is_colored', True)

to_check = [start]
while to_check:
    face = to_check[-1]
    to_check.pop()
    nbrs = mesh.face_neighbors(face)
    for nbr in nbrs:
        if mesh.face_attribute(nbr, 'is_colored') is None:
            to_check.append(nbr)
            if mesh.face_attribute(face, 'is_colored') is True:
                mesh.face_attribute(nbr, 'is_colored', False)
            elif mesh.face_attribute(face, 'is_colored') is False:
                mesh.face_attribute(nbr, 'is_colored', True)

facecolor = {}
for face in mesh.faces_where({'is_colored': True}):
    facecolor[face] = (0.7, 0.7, 0.7)
facecolor[start] = (1, 0.7, 0.7)

# plotter
plotter = Plotter()
artist = plotter.add(mesh,
                     facecolor=facecolor,
                     sizepolicy='relative',
                     vertexsize=0.5,
                     )

plotter.zoom_extents()
plotter.show()
