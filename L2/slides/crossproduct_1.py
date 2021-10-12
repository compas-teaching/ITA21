from math import radians
from compas.geometry import Point, Vector, Plane, Circle, Polygon
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

ab = a + b
axb = a.cross(b)
text = plotter.axes.text(1.2, 1.2, f'{axb[2]:+.3f}', fontsize=14)

area = Polygon([point, a, ab, b])
AREA = plotter.add(area, facecolor=(1, 0, 0), alpha=0.3)

R = Rotation.from_axis_and_angle([0, 0, 1], radians(2), point=point)

plotter.redraw(1)


@plotter.on(interval=0.05, frames=180)
def rotate(f):
    if f == 45 or f == 90 or f == 135:
        plotter.pause(1)

    b.transform(R)

    ab = a + b
    axb = a.cross(b)
    text.set_text(f'{axb[2]:+.3f}')

    area.points[2] = ab
    area.points[3] = b

    if axb[2] < 0 and AREA.facecolor[0] == 1:
        AREA.facecolor = (0, 0, 1)

    plotter.redraw()


plotter.show()