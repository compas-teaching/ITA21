import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

edge_width = {(1, 2): 3.0}
halfedges = [(1, 2), (2, 1)]
halfedge_color = {(1, 2): (1, 0, 0)}
vertex_color = {1: (1.0, 0.7, 0.7), 2: (1.0, 0.0, 0.0)}

meshartist = plotter.add(mesh, sizepolicy='absolute', edgewidth=edge_width, vertexcolor=vertex_color)

meshartist.draw_halfedges(halfedges=halfedges, color=halfedge_color)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
