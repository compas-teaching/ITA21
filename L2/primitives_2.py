from compas.geometry import Pointcloud
from compas.geometry import Plane, Circle, Ellipse
from compas.utilities import i_to_rgb
from compas_plotters import Plotter

plotter = Plotter(figsize=(16, 9), zstack='natural')

cloud = Pointcloud.from_bounds(x=16, y=9, z=0, n=13)

for index, point in enumerate(cloud):
    if index % 2:
        i = (index + 1) / 13
        radius = i
        circle = Circle(Plane(point, [0, 0, 1]), radius)
        plotter.add(circle,
                    facecolor=i_to_rgb(i, normalize=True),
                    edgecolor=i_to_rgb(1 - i, normalize=True))
    else:
        i = (index + 1) / 13
        major = 2 * i
        minor = i
        ellipse = Ellipse(Plane(point, [0, 0, 1]), major, minor)
        plotter.add(ellipse,
                    facecolor=i_to_rgb(i, normalize=True),
                    edgecolor=i_to_rgb(1 - i, normalize=True))

plotter.zoom_extents()
plotter.show()