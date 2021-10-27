from compas.geometry import Point, Vector, Line, Frame, Transformation
from compas_view2.app import App

world = Frame.worldXY()
local = Frame(Point(3, 2, 0), Vector(-1, 0, 0), Vector(0, -1, 0))

point = Point(2, 1, 0.5)

X = Transformation.from_change_of_basis(world, local)

for row in X.matrix:
    print(row)

local.transform(X)
world.transform(X)
point.transform(X)

print(local.xaxis)
print(world.xaxis)

