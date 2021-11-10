import os
import compas

from compas.geometry import Box
from compas.geometry import Transformation, Translation
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_4.json")
FILE_O = os.path.join(HERE, "assignment_5.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = ___
blank: Box = ___
table: Mesh = ___

# Place the blank and the mesh on the cutting table by
# 1. computing a frame-to-frame transformation between the frame of the blank and the frame of the table.
# 2. defining a translation over half the blank size in the y direction and half the blank size in the z direction
# 3. applying the combined transformation to both mesh and blank

X = Transformation.from_frame_to_frame(___, table.attributes['frame'])
T = Translation.from_vector([0, 0.5 * ___, 0.5 * ___])

mesh.transform(___ * ___)
blank.transform(___ * ___)

# Viz

viewer = App(width=1600, height=900)

viewer.view.camera.ty = 0
viewer.view.camera.tx = -1.2
viewer.view.camera.distance = 5

viewer.add(mesh, show_faces=True)
viewer.add(blank, opacity=0.5)
viewer.add(table, show_edges=True, facecolor=(0.9, 0.9, 0.9), linecolor=(1.0, 1.0, 1.0))
viewer.add(table.attributes['frame'], linewidth=10)

viewer.show()

# Export

compas.json_dump(data, FILE_O)
