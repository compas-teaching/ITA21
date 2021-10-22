import os
import compas
from math import radians

from compas.geometry import Point, Sphere
from compas.geometry import Translation, Scale, Rotation
from compas.datastructures import Mesh
from compas.utilities import i_to_rgb
from compas_view2.app import App
from compas_view2.objects import Collection

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))

vector = Point(0, 0, 0) - Point(*mesh.centroid())
vector[2] = 0

T = Translation.from_vector(vector)
S = Scale.from_factors([0.25, 0.25, 0.25])
R = Rotation.from_axis_and_angle([0, 0, 1], radians(90))

mesh.transform(R * S * T)

areas = [mesh.vertex_area(vertex) for vertex in mesh.vertices()]
amax = max(areas)

spheres = []
colors = []
for vertex in mesh.vertices():
    area = mesh.vertex_area(vertex)
    radius = area / amax
    color = i_to_rgb(radius, normalize=True)
    point = Point(*mesh.vertex_coordinates(vertex))
    sphere = Sphere(point, 0.1 * radius)
    spheres.append(sphere)
    colors.append(color)

viewer = App(width=1600, height=900)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -45
viewer.view.camera.distance = 10

viewer.add(mesh)

for sphere, color in zip(spheres, colors):
    viewer.add(sphere, facecolor=color)

viewer.show()