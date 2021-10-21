from math import radians
from compas.geometry import Point, Vector, Line, Polygon, Circle, Plane
from compas.geometry import Rotation
from compas.datastructures import Mesh
from compas_view2.app import App

viewer = App(width=1200, height=750)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -45
viewer.view.camera.distance = 4

circle = Circle(Plane([0, 0, 0], Vector.Zaxis()), 1.0)
viewer.add(circle, linewidth=2, u=128)

point = Point(0, 0, 0)
viewer.add(point)

a = Vector(1, 0, 0)
A = viewer.add(Line(point, a), color=(0, 0, 0), linewidth=5)

b = Vector(1, 0, 0)
B = viewer.add(Line(point, b), color=(0, 0, 0), linewidth=5)

ab = a + b

axb = a.cross(b)
AXB = viewer.add(Line(point, axb), color=(1, 0, 0), linewidth=5)

area = Polygon([point, a, ab, b])
AREA = viewer.add(area, show_face=True, facecolor=(1, 0, 0), opacity=0.3)

R = Rotation.from_axis_and_angle([0, 0, 1], radians(2), point=point)


@viewer.on(interval=100, frames=230)
def rotate(f):
    if f < 50:
        return

    b.transform(R)
    B._data.end = b

    ab = a + b

    axb = a.cross(b)
    AXB._data.end = axb

    if axb[2] < 0:
        AXB.linecolor = (0, 0, 1)
        AREA.facecolor = (0, 0, 1)

    AREA._data.points[2] = ab
    AREA._data.points[3] = b

    B.update()
    AXB.update()
    AREA.update()


viewer.show()