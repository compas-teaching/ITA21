from compas.geometry import Bezier, Polyline
from compas.geometry import Point, Vector, Box
from compas.geometry import Frame, Transformation
from compas.utilities import window

from compas_view2.app import App

curve = Bezier([Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)])

z = Vector.Zaxis()

P = curve.locus(resolution=50)
T = [(c - a).unitized() for a, b, c in window(P, 3) if a and c]
N = [z.cross(t) for t in T]
F = [Frame(p, t, n) for p, t, n in  zip(P, T, N)]
X = [Transformation.from_frame_to_frame(F[0], f) for f in F]

box = Box(F[0], 2, 1, 0.5)

viewer = App(width=800, height=900)
viewer.view.camera.rz = 90
viewer.view.camera.rx = -75
viewer.view.camera.tx = 0
viewer.view.camera.ty = -1
viewer.view.camera.distance = 6

viewer.add(Polyline(P), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True, linewidth=0.5)
viewer.add(box.frame)

boxobj = viewer.add(box, show_faces=True, opacity=0.5)

@viewer.on(interval=100, frames=len(F))
def move(f):
    x = X[f]
    viewer.add(F[f])
    boxobj.matrix = x.matrix
    boxobj.update()

viewer.show()
