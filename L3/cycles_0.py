import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 2

vertex_color = {VERTEX: (1.0, 0.0, 0.0)}

vertex_text = {}
for index, vertex in enumerate(mesh.vertex_neighbors(VERTEX)):
    vertex_text[vertex] = f'{index}'

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor=vertex_color)

meshartist.draw_vertexlabels(text=vertex_text)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
