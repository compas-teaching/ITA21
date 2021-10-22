import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=10, nx=10)

vertex_color = {vertex: (1.0, 0.0, 0.0) for vertex in mesh.vertices()}
vertex_color.update({vertex: (0.0, 0.0, 1.0) for vertex in mesh.vertices_on_boundary()})

plotter.add(mesh, sizepolicy='relative', vertexsize=10, vertexcolor=vertex_color)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
