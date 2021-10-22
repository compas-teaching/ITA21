import time
from math import radians
from compas.geometry import Point, Vector, Line, Plane, Circle, Polygon
from compas.geometry import Rotation
from compas_plotters import Plotter

point = Point(0, 0, 0)

a = Vector(1, 0, 0)
b = Vector(1, 0, 0)

R = Rotation.from_axis_and_angle([0, 0, 1], radians(45), point=point)
b.transform(R)

ab = a.dot(b)

print(ab)

circle = Circle(Plane(point, Vector.Zaxis()), 1.0)

b0 = b.copy()
b0[1] = 0
line = Line(b0, b)

plotter = Plotter(figsize=(12, 7.5), view=((-2, 2), (-2, 2)), show_axes=True)

plotter.add(point)
plotter.add(circle, fill=False)
plotter.add(a)
plotter.add(b)
plotter.add(line, draw_as_segment=True)

plotter.axes.text(1.1, 0.1, f'{ab:.3f}', fontsize=14)

plotter.show()