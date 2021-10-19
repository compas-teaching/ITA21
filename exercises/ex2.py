import os
import random
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

# deserialization
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'data', 'hexagon.json')
mesh = Mesh.from_json(FILE)

# select a random edge
start = random.choice(list(mesh.edges()))

# find edge strips
# ===================================================================================
# Modify the edge_strip(edge) algorithm for general n-gon meshes,
# which currently work for quad meshes.
# The algorithm should stop when n-gon with an odd number of sides is encountered

edges = mesh.edge_strip(start)
# ===================================================================================

# find strip faces
faces = []
for u, v in edges:
    if mesh.halfedge_face(u, v) is not None:
        faces.append(mesh.halfedge_face(u, v))

# visualize the edge strips
edgecolor = {}
for edge in edges:
    edgecolor[edge] = (0, 255, 0)
edgecolor[start] = (255, 0, 0)

# visualize the strip faces
facecolor = {}
for face in faces:
    facecolor[face] = (255, 200, 200)

# plotter
plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(radius=0.03)
plotter.draw_faces(facecolor=facecolor)
plotter.draw_edges(keys=edges, color=edgecolor, width=2.0)
plotter.show()
