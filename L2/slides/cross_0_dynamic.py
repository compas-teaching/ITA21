from math import radians
from compas.geometry import Point, Vector, Polygon
from compas.geometry import Rotation
from compas.datastructures import Mesh
from compas_view2.app import App
from compas_view2.shapes import Arrow

viewer = App(width=1200, height=750)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -65
viewer.view.camera.distance = 3

circle = Mesh.from_polygons([Polygon.from_sides_and_radius_xy(360, 1.0)])
viewer.add(circle, linewidth=2, facecolor=(1, 1, 1), show_faces=True, opacity=0.5)

point = Point(0, 0, 0)
viewer.add(point)

a = Vector(1, 0, 0)
A = viewer.add(Arrow(point, a, head_portion=0.2), show_edges=True, facecolor=(1, 0, 0), u=32)
a = A._data.direction

b = Vector(1, 0, 0)
B = viewer.add(Arrow(point, b, head_portion=0.2), show_edges=True, facecolor=(0, 1, 0), u=32)
b = B._data.direction

R = Rotation.from_axis_and_angle([0, 0, 1], radians(1), point=point)

c = a.cross(b)
C = None

@viewer.on(interval=100, frames=410)
def rotate(f):
    global c, C

    if f > 49:

        b.transform(R)
        c = a.cross(b)

        if f == 50:
            C = viewer.add(Arrow(point, c, head_portion=0.2), show_edges=True, facecolor=(0, 0, 1), u=32)

        else:
            C._data.direction = c

        B.update()
        C.update()


viewer.show()