import os
import compas

from compas.geometry import Frame, Box
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_3.json")
FILE_O = os.path.join(HERE, "assignment_4.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = data['mesh']
blank: Box = data['blank']

# Table

table = Mesh.from_meshgrid(dx=3, dy=4, nx=2, ny=2)
frame = Frame([1.5, 0, 0], [1, 0, 0], [0, 1, 0])

table.attributes['frame'] = frame

# Viz

viewer = App(width=1600, height=900)

viewer.view.camera.ty = 0
viewer.view.camera.tx = -1.2
viewer.view.camera.distance = 5

viewer.add(mesh)
viewer.add(blank, opacity=0.5)
viewer.add(blank.frame)
viewer.add(table, show_edges=True, facecolor=(0.9, 0.9, 0.9), linecolor=(1.0, 1.0, 1.0))
viewer.add(table.attributes['frame'], linewidth=10)
viewer.show()

# Export

data['table'] = table

compas.json_dump(data, FILE_O)
