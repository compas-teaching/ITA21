import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
VERTEX = 2

vertex_color = {VERTEX: (1.0, 0.0, 0.0)}
edge_color = {}
edge_width = {}

for nbr in mesh.vertex_neighbors(VERTEX):
    vertex_color[nbr] = (1.0, 0.9, 0.9)

for edge in mesh.vertex_edges(VERTEX):
    edge_color[edge] = (1.0, 0.0, 0.0)

for edge in mesh.vertex_edges(VERTEX):
    edge_width[edge] = 2.0

meshartist = plotter.add(mesh,
    vertexcolor=vertex_color,
    edgecolor=edge_color,
    edgewidth=edge_width,
    sizepolicy='absolute'
)

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
