import random
from compas.geometry import Pointcloud, Circle, Plane, Vector
from compas.utilities import i_to_red, i_to_green
from compas_plotters import Plotter

plotter = Plotter()

for point in Pointcloud.from_bounds(8, 5, 0, 53):
    radius = random.random()
    circle = Circle(Plane(point, Vector(0, 0, 1)), radius)

    plotter.add(circle,
                facecolor=i_to_red(radius, normalize=True),
                edgecolor=i_to_green(1 - radius, normalize=True))

plotter.zoom_extents()
plotter.show()
