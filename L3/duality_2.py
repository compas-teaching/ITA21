import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
dual = mesh.dual()

meshartist = plotter.add(mesh, sizepolicy='absolute', show_faces=False)
dualartist = plotter.add(dual, sizepolicy='absolute')

dualartist.draw_vertexlabels()

plotter.zoom_extents()
plotter.show()

# plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
