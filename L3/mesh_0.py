import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_meshgrid(dx=2, nx=2)

plotter = Plotter(figsize=(8, 8))
plotter.add(mesh, sizepolicy='absolute')
plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
