import os
import compas

from compas.geometry import Point, Line, Box
from compas.geometry import dot_vectors
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_5.json")
FILE_O = os.path.join(HERE, "assignment_6.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = ___
blank: Box = ___
table: Mesh = ___

# Find the left face of the mesh in the current orientation.

left = sorted(___, key=lambda face: ___)[___]

# Identify the vertices of the left face.

left_vertices = ___

# Identify the bottom-front most vertex of the left face (left-bottom-front => lbf).

lbf = sorted(___, key=lambda vertex: mesh.vertex_coordinates(vertex, 'zy'))[0]

lbf_point = Point(* mesh.vertex_coordinates(lbf))

# Find the index of the lbf in the list of vertices of the left face.

lbf_index = ___.index(___)

# Reorder the vertices of the left face such that they start at the lbf.

left_cycle = left_vertices[___:] + left_vertices[:___]

# Identify the matching right cycle
# by finding for each vertex of the left cycle
# a neighbouring vertex that does not belong to the left cycle.

right_cycle = []
for vertex in ___:
    for nbr in mesh.___(vertex):
        if nbr not in ___:
            ___.append(nbr)
            break

# Viz

viewer = App(width=1600, height=900)
viewer.view.camera.rz = +50
viewer.view.camera.rx = -70
viewer.view.camera.ty = -0.7
viewer.view.camera.distance = 1.8

viewer.add(mesh, facecolors={left: (0, 1, 1)})
viewer.add(blank, opacity=0.5)
viewer.add(table, show_edges=True, facecolor=(0.9, 0.9, 0.9), linecolor=(1.0, 1.0, 1.0))
viewer.add(lbf_point, size=20, color=(1, 0, 0))

# Draw a line between matching vertices of left and right cycle.

for u, v in zip(___, ___):
    a = mesh.vertex_coordinates(u)
    b = mesh.vertex_coordinates(v)
    viewer.add(___, linewidth=10, color=(1, 0, 0))

viewer.show()

# Export

mesh.attributes['cycles'] = {'left': left_cycle, 'right': right_cycle}

compas.json_dump(data, FILE_O)
