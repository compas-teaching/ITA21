import os

from compas.geometry import Point, Polygon
from compas.datastructures import Mesh, halfedge
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
    right = mesh.halfedge_face(nbr, VERTEX)

    b = Point(* mesh.vertex_coordinates(nbr))
    ab = b - a
    ab.scale(0.5)

    c = Point(* mesh.face_centroid(right))
    ac = c - a

    plotter.add(ab, point=a)
    plotter.add(ac, point=a)

    plotter.add(Polygon([a, a + ab, a + ac]), facecolor=(1.0, 1.0, 1.0), zorder=2000)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
