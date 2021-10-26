import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

edge_width = {(1, 2): 3.0}

meshartist = plotter.add(mesh, sizepolicy='absolute', edgewidth=edge_width)

meshartist.draw_vertexlabels()
meshartist.draw_edgelabels()

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
