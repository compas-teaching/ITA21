import os
import compas

from compas.geometry import Point, Line, Polyline, Plane, Box
from compas.geometry import dot_vectors
from compas.geometry import intersection_line_plane
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_6.json")
FILE_O = os.path.join(HERE, "assignment_7.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = ___
blank: Box = ___
table: Mesh = ___

left_cycle = mesh.attributes[___][___]
right_cycle = mesh.attributes[___][___]

# Planes

left_plane = Plane([0, 0, 0], [-1, 0, 0])
right_plane = Plane([3, 0, 0], [+1, 0, 0])

# Wire

wires = [(left_plane.point, right_plane.point)]

# Compute the full wires
# by intersecting the line segments defined by matching left and right vertices
# with the left and right plane.

for u, v in zip(___, ___):
    a = mesh.vertex_coordinates(u)
    b = mesh.vertex_coordinates(v)
    line = Line(a, b)

    a = Point(* intersection_line_plane(line, ___))
    b = Point(* intersection_line_plane(line, ___))

    wires.append((a, b))

wires.append(wires[1])
wires.append(wires[0])

# Viz

viewer = App(width=1600, height=900)
viewer.view.camera.rz = +50
viewer.view.camera.rx = -70
viewer.view.camera.ty = -0.7
viewer.view.camera.distance = 1.8

viewer.add(mesh)
viewer.add(blank, opacity=0.5)
viewer.add(table, show_edges=True, facecolor=(0.9, 0.9, 0.9), linecolor=(1.0, 1.0, 1.0))

for a, b in wires:
    viewer.add(Line(a, b), linewidth=10, color=(1, 0, 0))

# a, b = zip(*wires)

# viewer.add(Polyline(a), linewidth=3, show_points=True)
# viewer.add(Polyline(b), linewidth=3, show_points=True)

viewer.show()

# Export

data['wires'] = wires

compas.json_dump(data, FILE_O)
