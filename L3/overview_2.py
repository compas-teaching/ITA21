from math import radians
import compas
from compas.geometry import Point, Line
from compas.datastructures import Mesh
from compas.topology import shortest_path
from compas.utilities import pairwise
from compas.geometry import Scale, Translation, Rotation

from compas_view2.app import App

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
centroid = Point(* mesh.centroid())
vector = Point(0, 0, 0) - centroid
vector[2] = 0

T = Translation.from_vector(vector)
R = Rotation.from_axis_and_angle([0, 0, 1], radians(90))
S = Scale.from_factors([0.3, 0.3, 0.3])

mesh.transform(S * R * T)

viewer = App(width=1600, height=900)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.tx = 0
viewer.view.camera.ty = 0
viewer.view.camera.distance = 12

viewer.add(mesh)

start = 126

a = Point(* mesh.vertex_coordinates(start))
viewer.add(a, size=20, color=(1, 0, 0))

end = mesh.vertex_sample()[0]

path = shortest_path(mesh.halfedge, start, end)

for u, v in pairwise(path):
    a = Point(* mesh.vertex_coordinates(u))
    b = Point(* mesh.vertex_coordinates(v))
    ab = Line(a, b)

    viewer.add(b, size=20, color=(0, 0, 1))
    viewer.add(ab, linewidth=10, linecolor=(0, 1, 0))


viewer.show()
