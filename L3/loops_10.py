import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=10, nx=10)

edge = 12, 13
loop = mesh.edge_loop(edge)

vertex_color = {}
edge_width = {}
for u, v in loop:
    vertex_color[u] = (1.0, 0.7, 0.7)
    edge_width[u, v] = 3.0

vertex_color[v] = (1.0, 0.0, 0.0)

meshartist = plotter.add(mesh, sizepolicy='relative', edgewidth=edge_width, vertexcolor=vertex_color, vertexsize=10)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
