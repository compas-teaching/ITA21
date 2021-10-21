from math import radians
from compas.geometry import Point, Vector, Line, Polygon, Circle, Plane
from compas.geometry import Rotation
from compas.datastructures import Mesh
from compas_view2.app import App

point = Point(0, 0, 0)

a = Vector(1, 0, 0)
b = Vector(1, 0, 0)

R = Rotation.from_axis_and_angle([0, 0, 1], radians(45), point=point)
b.transform(R)

ab = a + b

axb = a.cross(b)
poly = Polygon([point, a, ab, b])

print(axb.length == poly.area)
print(axb.dot(Vector.Zaxis()) > 0)

circle = Circle(Plane([0, 0, 0], Vector.Zaxis()), 1.0)

viewer = App(width=1200, height=750)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -45
viewer.view.camera.distance = 4

viewer.add(circle, linewidth=2, u=128)
viewer.add(point)
viewer.add(Line(point, a), color=(0, 0, 0), linewidth=5)
viewer.add(Line(point, b), color=(0, 0, 0), linewidth=5)
viewer.add(Line(point, axb), color=(1, 0, 0), linewidth=5)
viewer.add(poly, show_face=True, facecolor=(1, 0, 0), opacity=0.3)

viewer.show()