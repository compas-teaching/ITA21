from compas.geometry import Bezier, Polyline
from compas.geometry import Point, Vector, Box
from compas.geometry import Frame, Transformation
from compas.utilities import window

from compas_view2.app import App

controlpoints = [Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)]
curve = Bezier(controlpoints)

up = Vector.Zaxis()

points = curve.locus(resolution=83)
tangents = [(c - a).unitized() for a, b, c in window(points, 3) if a and c]
normals = [up.cross(vector) for vector in tangents]
frames = [Frame(p, t, n) for p, t, n in  zip(points[1:], tangents, normals)]
xforms = [Transformation.from_frame_to_frame(frames[0], frame) for frame in frames]

box = Box(frames[0], 2, 1, 0.5)

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 90
viewer.view.camera.rx = -75
viewer.view.camera.tx = 0
viewer.view.camera.ty = -1
viewer.view.camera.distance = 6

viewer.add(Polyline(points), linewidth=3)
viewer.add(Polyline(controlpoints), show_points=True, linewidth=0.5)

BOX = viewer.add(box, show_faces=True, opacity=0.5)
FRAME = viewer.add(box.frame)

@viewer.on(interval=100, frames=len(frames))
def move(f):

    X = xforms[f]

    viewer.add(frames[f])
    BOX.matrix = X.matrix
    BOX.update()

viewer.show()
