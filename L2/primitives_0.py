from compas.geometry import Pointcloud
from compas.geometry import Vector, Line, Plane, Circle, Ellipse, Polyline, Polygon
from compas.geometry import Translation
from compas.utilities import i_to_black

from compas_plotters import Plotter

cloud = Pointcloud.from_bounds(16, 9, 0, 9)

vector = cloud[1] - cloud[0]
line = Line(cloud[0], cloud[1])

circle = Circle(Plane(cloud[1], Vector(0, 0, 1)), 1.0)
ellipse = Ellipse(Plane(cloud[2], Vector(0, 0, 1)), 2.0, 1.0)

triangle = Polygon.from_sides_and_radius_xy(3, 1.0).transformed(Translation.from_vector(cloud[3]))
square = Polygon.from_sides_and_radius_xy(4, 1.0).transformed(Translation.from_vector(cloud[4]))
pentagon = Polygon.from_sides_and_radius_xy(5, 1.0).transformed(Translation.from_vector(cloud[5]))
hexagon = Polygon.from_sides_and_radius_xy(6, 1.0).transformed(Translation.from_vector(cloud[6]))
heptagon = Polygon.from_sides_and_radius_xy(7, 1.0).transformed(Translation.from_vector(cloud[7]))
octagon = Polygon.from_sides_and_radius_xy(8, 1.0).transformed(Translation.from_vector(cloud[8]))

plotter = Plotter(figsize=(16, 9))

plotter.add(Polyline(cloud), linestyle='dotted', linewidth=0.5)
plotter.add(vector.unitized(), point=cloud[0])
# plotter.add(line, draw_as_segment=False, linestyle='dashed', linewidth=1)
plotter.add(line, draw_as_segment=True, linewidth=1)
plotter.add(circle, alpha=0.5, facecolor=i_to_black(0, normalize=True))
plotter.add(ellipse, alpha=0.5, facecolor=i_to_black(0.1, normalize=True))
plotter.add(triangle, alpha=0.5, facecolor=i_to_black(0.2, normalize=True))
plotter.add(square, alpha=0.5, facecolor=i_to_black(0.3, normalize=True))
plotter.add(pentagon, alpha=0.5, facecolor=i_to_black(0.4, normalize=True))
plotter.add(hexagon, alpha=0.5, facecolor=i_to_black(0.5, normalize=True))
plotter.add(heptagon, alpha=0.5, facecolor=i_to_black(0.6, normalize=True))
plotter.add(octagon, alpha=0.5, facecolor=i_to_black(0.7, normalize=True))

plotter.zoom_extents()
plotter.show()
