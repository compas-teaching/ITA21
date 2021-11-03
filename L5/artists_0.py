from math import radians
import compas
from compas.geometry import Point
from compas.datastructures import Mesh
from compas.geometry import Scale, Translation, Rotation

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
centroid = Point(* mesh.centroid())
vector = Point(0, 0, 0) - centroid
vector[2] = 0

T = Translation.from_vector(vector)
R = Rotation.from_axis_and_angle([0, 0, 1], radians(90))
S = Scale.from_factors([0.3, 0.3, 0.3])

mesh.transform(S * R * T)

compas.json_dump(mesh, 'L5/tubemesh.json')
