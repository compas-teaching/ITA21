import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 2

nbrs = mesh.vertex_neighbors(VERTEX)

vertex_color = {
    VERTEX: (1.0, 0.0, 0.0),
    nbrs[0]: (0.0, 0.0, 1.0)
}

vertex_text = {}
for index, vertex in enumerate(nbrs):
    vertex_text[vertex] = f'{index}'

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor=vertex_color)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
