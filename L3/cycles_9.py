import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 2

sorted_nbrs = []
nbrs = mesh.vertex_neighbors(VERTEX)

sorted_nbrs.append(nbrs.pop(0))

v, w = mesh.halfedge_after(sorted_nbrs[-1], VERTEX)
sorted_nbrs.append(w)

v, w = mesh.halfedge_after(sorted_nbrs[-1], VERTEX)
sorted_nbrs.append(w)

v, w = mesh.halfedge_after(sorted_nbrs[-1], VERTEX)
sorted_nbrs.append(w)

halfedges = [
    (VERTEX, sorted_nbrs[0]),
    (sorted_nbrs[0], VERTEX),
    (VERTEX, sorted_nbrs[1]),
    (sorted_nbrs[1], VERTEX),
    (VERTEX, sorted_nbrs[2]),
    (sorted_nbrs[2], VERTEX),
    (VERTEX, sorted_nbrs[3]),
    (sorted_nbrs[3], VERTEX),
]

halfedge_color = {
    halfedges[7]: (0, 0, 0),
}

vertex_color = {
    VERTEX: (1.0, 0.0, 0.0),
    sorted_nbrs[0]: (0.0, 0.0, 1.0),
    sorted_nbrs[1]: (0.0, 0.0, 1.0),
    sorted_nbrs[2]: (0.0, 0.0, 1.0),
    sorted_nbrs[3]: (0.0, 0.0, 1.0),
}

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor=vertex_color)

meshartist.draw_halfedges(halfedges=halfedges, color=halfedge_color)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
