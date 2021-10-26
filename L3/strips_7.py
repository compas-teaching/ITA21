import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

u, v = 4, 5

vertex_color = {u: (1.0, 0.7, 0.7), v: (1.0, 0.0, 0.0)}

halfedges = [(u, v), (v, u)]

edge_width = {(u, v): 3.0}

t, u = mesh.halfedge_before(u, v)
s, t = mesh.halfedge_before(t, u)

edge_width[t, s] = 3.0

u, v = t, s

t, u = mesh.halfedge_before(u, v)
s, t = mesh.halfedge_before(t, u)

edge_width[t, s] = 3.0

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor=vertex_color, edgewidth=edge_width)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
