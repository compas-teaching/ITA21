from math import radians
import compas
from compas.geometry import Point, Line
from compas.datastructures import Mesh
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
mesh.flip_cycles()

viewer = App(width=1600, height=900)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.tx = 0
viewer.view.camera.ty = 0
viewer.view.camera.distance = 12

viewer.add(mesh)

start = 126, 1

for edge in mesh.edge_loop(start):
    a, b = mesh.edge_coordinates(*edge)
    line = Line(a, b)

    viewer.add(line, linewidth=10, linecolor=(0, 1, 0))

viewer.show()
