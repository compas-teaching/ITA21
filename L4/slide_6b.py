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
        T.append(t)
        N.append(n)

frames = []
for p, t, n in zip(points[1:-1], T, N):
    frames.append(Frame(p, t, n))

base = frames[0]

xforms = []
for frame in frames[1:]:
    xforms.append(Transformation.from_frame_to_frame(base, frame))

box = Box(base, 2, 1, 0.5)

box.transform(xforms[1])

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 90
viewer.view.camera.rx = -75
viewer.view.camera.tx = 0
viewer.view.camera.ty = -1
viewer.view.camera.distance = 6

viewer.add(Polyline(curve.locus()), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True, linewidth=0.5)

viewer.add(base, linewidth=3)

viewer.add(box, show_faces=True, opacity=0.5)
viewer.add(box.frame)

viewer.show()
