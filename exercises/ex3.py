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

# visualization face settings
facecolor = {}
facecolor[start] = (1, 0.7, 0.7)
# Hint3: visualize the faces based on the face attribute you set. 

# plotter
plotter = Plotter()
artist = plotter.add(mesh,
                     facecolor=facecolor,
                     sizepolicy='relative',
                     vertexsize=0.5,
                     )

plotter.zoom_extents()
plotter.show()