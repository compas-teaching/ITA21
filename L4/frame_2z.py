from compas.geometry import Point, Line, Polygon, Frame
from compas_view2.app import App

world = Frame.worldXY()

point = Point(2, 1, 0.5)

xy = point.copy()
xy[2] = 0

x = world.xaxis * world.xaxis.dot(point - world.point)
y = world.yaxis * world.yaxis.dot(point - world.point)
z = world.zaxis * world.zaxis.dot(point - world.point)

viewer = App(width=800, height=900)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -60
viewer.view.camera.tx = -2
viewer.view.camera.distance = 8

viewer.add(world, linewidth=5)
viewer.add(point, size=20)

viewer.add(Line(world.point, point), linewidth=2)
viewer.add(Line(point, xy), linewidth=2)
viewer.add(Line(xy, x), linewidth=2)
viewer.add(Line(xy, y), linewidth=2)

viewer.add(Polygon([world.point, point, z]), facecolor=(0.0, 0.0, 1.0), opacity=0.3)

viewer.show()
