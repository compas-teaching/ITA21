from compas.geometry import Point, Line, Polyline, Bezier, Box
from compas.geometry import Frame, Transformation
from compas.utilities import window

from compas_view2.app import App

curve = Bezier([Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)])

points = curve.locus(resolution=50)

T = []
N = []
for a, b, c in window(points, 3):
    if a and c:
        t = c - a
        n = (c - b).cross(a - b).cross(t)
        T.append(t.unitized())
        N.append(n.unitized())

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 90
viewer.view.camera.rx = -75
viewer.view.camera.tx = 0
viewer.view.camera.ty = -1
viewer.view.camera.distance = 6

viewer.add(Polyline(curve.locus()), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True, linewidth=0.5)

for point in points:
    viewer.add(point)

for p, t, n in zip(points[1:-1], T, N):
    viewer.add(Line(p, p + t), color=(1, 0, 0), linewidth=3)
    viewer.add(Line(p, p + n), color=(0, 1, 0), linewidth=3)

viewer.show()
