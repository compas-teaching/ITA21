import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
UV = 2, 6

face_color = {mesh.halfedge_face(*UV): (1.0, 0.7, 0.7)}

meshartist = plotter.add(mesh, sizepolicy='absolute', facecolor=face_color)

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=[UV], color={UV: (1.0, 0.0, 0.0)})

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
