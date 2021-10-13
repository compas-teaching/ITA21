from compas.geometry import Pointcloud
from compas.geometry import Line, Polyline
from compas.utilities import pairwise
from compas_plotters import Plotter

plotter = Plotter(figsize=(16, 9), zstack='zorder')

cloud = Pointcloud.from_bounds(x=16, y=9, z=0, n=13)

plotter.add(Polyline(cloud), show_points=False, color=(1, 0, 0))

for index, (a, b) in enumerate(pairwise(cloud)):
    vector = (b - a).unitized()
    line = Line(a, b)

    plotter.add(a, facecolor=(1, 0, 0))
    plotter.add(line, show_points=False, linewidth=0.5, linestyle='dotted', color=(1, 0, 0))
    plotter.add(vector, point=a, show_point=False, color=(1, 0, 0))

plotter.add(cloud[-1], facecolor=(1, 0, 0))

plotter.zoom_extents()
plotter.show()