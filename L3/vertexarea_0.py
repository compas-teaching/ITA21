import os

from compas.geometry import Point
from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 2

halfedges = []
for nbr in mesh.vertex_neighbors(VERTEX):
    halfedges.append((VERTEX, nbr))
    halfedges.append((nbr, VERTEX))

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor={VERTEX: (1.0, 0.0, 0.0)})
meshartist.draw_halfedges(halfedges=halfedges)

a = Point(*mesh.vertex_coordinates(VERTEX))
plotter.add(a)

for nbr in mesh.vertex_neighbors(VERTEX):
    b = Point(* mesh.vertex_coordinates(nbr))
    ab = b - a
    ab.scale(0.5)

    plotter.add(ab, point=a)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
