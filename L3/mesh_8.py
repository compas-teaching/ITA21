import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

U, V = 2, 6
T, U = mesh.halfedge_before(U, V)

halfedges = [(T, U), (U, V), (U, T)]

face_color = {
    mesh.halfedge_face(T, U): (1.0, 0.7, 0.7),
    mesh.halfedge_face(U, T): (0.7, 0.7, 1.0)
}

halfedge_color = {
    (T, U): (1.0, 0.0, 0.0),
    (U, V): (1.0, 0.0, 0.0),
    (U, T): (0.0, 0.0, 1.0)
}

meshartist = plotter.add(mesh, sizepolicy='absolute', facecolor=face_color)

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=halfedges, color=halfedge_color)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
