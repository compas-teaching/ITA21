import os
import compas

from compas.geometry import Line, Box
from compas.datastructures import Mesh
from compas.utilities import pairwise, linspace

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_7.json")

data = compas.json_load(FILE_I)

# Load data

mesh: Mesh = ___
blank: Box = ___
table: Mesh = ___

wires = ___

# Interpolation

A, B = zip(*wires)

interpolation = []

# Zip together pairs of points on cycle A and cycle B.

for (___, ___), (___, ___) in zip(pairwise(___), pairwise(___)):

    # For each vector between pairs of points
    a_aa = aa - a
    b_bb = bb - b

    # Identify the length of the longest of the two
    # compute the approximate number of steps required to move 0.01 units at a time.

    l = max(___, ___)
    n = int(l / ___)

    for i in linspace(0, 1, num=n):
        if i == 0:
            continue

        ai = a + a_aa * i
        bi = b + b_bb * i

        interpolation.append((ai, bi))
    
# Viz

viewer = App(width=1600, height=900)
viewer.view.camera.rz = +50
viewer.view.camera.rx = -70
viewer.view.camera.ty = -0.7
viewer.view.camera.distance = 1.8

viewer.add(mesh)
viewer.add(blank, opacity=0.5)
viewer.add(table, show_edges=True, facecolor=(0.9, 0.9, 0.9), linecolor=(1.0, 1.0, 1.0))

@viewer.on(interval=10, frames=len(___))
def cut(i):
    a, b = interpolation[___]
    viewer.add(Line(a, b), color=(1, 0, 0))

viewer.show()
