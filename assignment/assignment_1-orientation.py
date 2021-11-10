import os
import compas

from compas.geometry import dot_vectors
from compas.datastructures import Mesh
from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_0.json")
FILE_O = os.path.join(HERE, "assignment_1.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = data[___]

# Update defaults

mesh.update_default_face_attributes(left=False)
mesh.update_default_face_attributes(top=False)
mesh.update_default_face_attributes(front=False)

# Identify left

# Sort the faces based on the size of the dot product
# of the unitized face normal and the negative X axis.
# The last element of the sorted list has the highest value
# and thus is the "most parallel" with this direction.

left = sorted(___, key=lambda face: dot_vectors(___, ___))[___]

mesh.face_attribute(left, 'left', True)

# Identify top

# Sort the faces based on the size of the dot product
# of the unitized face normal and the positive Z axis.
# The last element of the sorted list has the highest value
# and thus is the "most parallel" with this direction.

top = sorted(___, key=lambda face: dot_vectors(___, ___))[___]

mesh.face_attribute(top, 'top', True)

# Identify front

# Sort the faces based on the size of the dot product
# of the unitized face normal and the positive Z axis.
# The last element of the sorted list has the highest value
# and thus is the "most parallel" with this direction.

front = sorted(___, key=lambda face: dot_vectors(___, ___))[___]

mesh.face_attribute(front, 'front', True)

# Viz

viewer = App(width=1600, height=900)
viewer.view.camera.rz = 25
viewer.view.camera.rx = -65
viewer.view.camera.ty = -0.8
viewer.view.camera.tx = 0
viewer.view.camera.distance = 3

# Color
# left: blue
# top: red
# front: green

viewer.add(mesh, facecolors={left: ___, top: ___, front: ___})
viewer.show()

# Export

compas.json_dump(data, FILE_O)
