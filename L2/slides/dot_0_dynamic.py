import time
from math import radians
from compas.geometry import Point, Vector, Line, Plane, Circle, Polygon
from compas.geometry import Rotation
from compas_plotters import Plotter

# how big is the component of one vector in the direction of another

plotter = Plotter(figsize=(12, 7.5), view=((-2, 2), (-2, 2)), show_axes=True)

point = Point(0, 0, 0)
plotter.add(point)

circle = Circle(Plane(point, Vector.Zaxis()), 1.0)
plotter.add(circle, fill=False)

a = Vector(1, 0, 0)
b = Vector(1, 0, 0)

plotter.add(a)
plotter.add(b)

line = Line(a, b)

ab = a.dot(b)
text = plotter.axes.text(1.1, 0.1, f'{ab:.3f}', fontsize=14)

R = Rotation.from_axis_and_angle([0, 0, 1], radians(2), point=point)

plotter.redraw(1)


@plotter.on(interval=0.05, frames=180)
def rotate(f):
    if f == 45 or f == 90 or f == 135:
        plotter.pause(1)

    b.transform(R)
    
    line.end = b
    line.start[0] = b[0]

    if f == 0:
        plotter.add(line, draw_as_segment=True)
    
    ab = a.dot(b)
    text.set_text(f'{ab:.3f}')

    plotter.redraw()


plotter.show()