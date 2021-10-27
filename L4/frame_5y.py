from compas.geometry import Point, Vector, Line, Polygon, Frame, Transformation
from compas_view2.app import App

world = Frame.worldXY()
local = Frame(Point(3, 2, 0), Vector(-1, 0, 0), Vector(0, -1, 0))

point = Point(2, 1, 0.5)

X = Transformation.from_change_of_basis(world, local)

local.transform(X)
world.transform(X)
point.transform(X)

xy = point.copy()
xy[2] = 0

x = local.xaxis * local.xaxis.dot(point - local.point)
y = local.yaxis * local.yaxis.dot(point - local.point)
z = local.zaxis * local.zaxis.dot(point - local.point)

viewer = App(width=800, height=900)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -60
viewer.view.camera.tx = -2
viewer.view.camera.distance = 8

viewer.add(world, linewidth=5)
viewer.add(local, linewidth=5)

viewer.add(point, size=20)

viewer.add(Line(local.point, point), linewidth=2)
viewer.add(Line(point, xy), linewidth=2)
viewer.add(Line(xy, local.point + x), linewidth=2)
viewer.add(Line(xy, local.point + y), linewidth=2)

viewer.add(Polygon([local.point, point, local.point + y]), facecolor=(0.0, 1.0, 0.0), opacity=0.3)

viewer.show()
