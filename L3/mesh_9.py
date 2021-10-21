import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
U, V = 2, 6
V, W = mesh.halfedge_after(U, V)

face_color = {
    mesh.halfedge_face(V, W): (1.0, 0.7, 0.7),
}

meshartist = plotter.add(mesh, sizepolicy='absolute', facecolor=face_color)

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=[(U, V), (V, W), (W, V)], color={(U, V): (1.0, 0.0, 0.0), (V, W): (1.0, 0.0, 0.0), (W, V): (0.0, 0.0, 1.0)})

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
