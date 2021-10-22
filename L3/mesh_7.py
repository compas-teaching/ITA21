import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
FACE = 2

meshartist = plotter.add(mesh, sizepolicy='absolute', facecolor={FACE: (1.0, 0.7, 0.7)})

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(halfedges=mesh.face_halfedges(FACE), color=(1.0, 0.0, 0.0))

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
