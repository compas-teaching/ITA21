import random
from compas.geometry import Point, Vector, Line, Plane, Circle
from compas.geometry import Pointcloud, Frame, Translation
from compas.geometry import Box, Sphere, Cylinder, Cone, Capsule, Polyhedron, Torus
from compas.utilities import i_to_rgb

from compas_view2.app import App

viewer = App()

shapes = [
    Box(Frame.worldXY(), 1, 1, 1),
    Sphere(Point(0, 0, 0), 1.0),
    Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.3), 1.0),
    Cone(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.3), 1.0),
    Capsule(Line(Point(0, 0, 0), Point(0, 0, 1)), 0.2),
    Polyhedron.from_platonicsolid(12),
    Torus(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 1.0, 0.3)
]

for point in Pointcloud.from_bounds(16, 9, 3, 23):
    X = Translation.from_vector(point)
    shape = random.choice(shapes)
    viewer.add(shape.transformed(X), facecolor=i_to_rgb(random.random(), normalize=True))

viewer.show()
