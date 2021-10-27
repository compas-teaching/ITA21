from compas.geometry import Point, Line, Polyline, Bezier, Box
from compas.geometry import Frame, Transformation
from compas.utilities import window

from compas_view2.app import App

curve = Bezier([Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)])

points = curve.locus(resolution=50)

a, b, c = points[1:4]

t = c - a
n = (c - b).cross(a - b).cross(t)

t.unitize()
n.unitize()

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 90
viewer.view.camera.rx = -75
viewer.view.camera.tx = 0
viewer.view.camera.ty = -1
viewer.view.camera.distance = 6

viewer.add(Polyline(curve.locus()), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True, linewidth=0.5)

viewer.add(a, size=20)
viewer.add(b, size=20)
viewer.add(c, size=20)

for point in points[0:1] + points[4:]:
    viewer.add(point)

viewer.add(Line(b, b + t), color=(1, 0, 0), linewidth=3)
viewer.add(Line(b, b + n), color=(0, 1, 0), linewidth=3)

viewer.show()
