from compas.geometry import Point, Vector, Line, Frame
from compas_view2.app import App

world = Frame.worldXY()

point = Point(2, 1, 0.5)

xy = point.copy()
xy[2] = 0

x = point.copy()
x[1] = 0
x[2] = 0

y = point.copy()
y[0] = 0
y[2] = 0

z = point.copy()
z[0] = 0
z[1] = 0

viewer = App(width=800, height=900)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -60
viewer.view.camera.tx = -2
viewer.view.camera.distance = 8

viewer.add(world, linewidth=5)
viewer.add(point, size=20)

viewer.add(Line(point, xy), linewidth=2)
viewer.add(Line(xy, x), linewidth=2)
viewer.add(Line(xy, y), linewidth=2)

viewer.show()
