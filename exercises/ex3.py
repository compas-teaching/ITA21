import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

# deserialization
mesh = Mesh.from_obj(compas.get('faces.obj'))

# pick a random vertex from the mesh
vertex = mesh.get_any_vertex()

# step 1: pick a face connected to the vertex
# hint: Mesh.vertex_faces


# Step 2: develop checkered pattern starting from the face you find in step 1
# checkered pattern contains two colors where a single checker is surrounded 
# on all four sides by a checker of a different color.

# Hint1: you can set a face attribute to the start face, e.g. "is_colored": True.
# then set attribute to the neighbour faces, e.g. "is_colored": False.
# To should avoid an infitie loop, you should find a way to check the face and its neighbours only once

# Hint2: Mesh.face_neighbors, Mesh.update_default_face_attribute, Mesh.face_attribute

# visualization
vertexcolor = {}
vertexcolor[vertex] = (255, 0, 0)

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(facecolor=vertexcolor)
plotter.draw_faces()
plotter.show()