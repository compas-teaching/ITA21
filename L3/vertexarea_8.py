import os

from compas.geometry import Point, Polygon
from compas.datastructures import Mesh
from compas.utilities import i_to_rgb
from compas.utilities.itertools import pairwise
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

areas = [mesh.vertex_area(vertex) for vertex in mesh.vertices()]
amax = max(areas)

vertex_color = {}
for vertex in mesh.vertices():
    area = mesh.vertex_area(vertex)
    color = i_to_rgb(area / amax, normalize=True)
    vertex_color[vertex] = color

    a = Point(* mesh.vertex_coordinates(vertex))

    plotter.add(a, size=25, facecolor=color)

    nbrs = mesh.vertex_neighbors(vertex, ordered=True)

    if len(nbrs) == 2:
        b = mesh.edge_midpoint(vertex, nbrs[0])
        c = mesh.face_centroid(mesh.halfedge_face(nbrs[0], vertex))
        d = mesh.edge_midpoint(vertex, nbrs[1])
        plotter.add(Polygon([a, b, c]), facecolor=color, zorder=2000, alpha=0.3)
        plotter.add(Polygon([a, c, d]), facecolor=color, zorder=2000, alpha=0.3)

    elif len(nbrs) == 3:
        b = mesh.edge_midpoint(vertex, nbrs[0])
        c = mesh.face_centroid(mesh.halfedge_face(nbrs[0], vertex))
        d = mesh.edge_midpoint(vertex, nbrs[1])
        e = mesh.face_centroid(mesh.halfedge_face(nbrs[1], vertex))
        f = mesh.edge_midpoint(vertex, nbrs[2])
        plotter.add(Polygon([a, b, c]), facecolor=color, zorder=2000, alpha=0.3)
        plotter.add(Polygon([a, c, d]), facecolor=color, zorder=2000, alpha=0.3)
        plotter.add(Polygon([a, d, e]), facecolor=color, zorder=2000, alpha=0.3)
        plotter.add(Polygon([a, e, f]), facecolor=color, zorder=2000, alpha=0.3)

    else:
        points = []
        for nbr in nbrs:
            b = mesh.edge_midpoint(vertex, nbr)
            c = mesh.face_centroid(mesh.halfedge_face(nbr, vertex))
            points.append(b)
            points.append(c)

        for b, c in pairwise(points + points[:1]):
            plotter.add(Polygon([a, b, c]), facecolor=color, zorder=2000, alpha=0.3)

for face in mesh.faces():
    point = Point(* mesh.face_centroid(face))
    plotter.add(point, size=10)

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexsize=7.5, vertexcolor=vertex_color, show_vertices=False)

meshartist.draw_vertexlabels(text={vertex: f'{mesh.vertex_area(vertex):.1f}' for vertex in mesh.vertices()})

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
