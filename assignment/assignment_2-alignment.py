import os
import compas

from math import radians

from compas.geometry import bestfit_frame_numpy
from compas.geometry import Frame, Rotation, Transformation
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_1.json")
FILE_O = os.path.join(HERE, "assignment_2.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = ___

left = list(mesh.faces_where({___: ___}))[0]
top = list(mesh.faces_where({___: ___}))[0]
front = list(mesh.faces_where({___: ___}))[0]

# Compute a bestfit frame for the left face of the mesh
# Use the coordinates of the corners of the face as input for the bestfit function.

frame = Frame(*bestfit_frame_numpy(___))

# Since the face is 2D,
# the frame might be roto-reflected.
# If that is the case, rotate it by 180 degrees around the frame y axis.

if frame.zaxis.dot([1, 0, 0]) < 0:
    R = Rotation.from_axis_and_angle(___, radians(___), point=frame.point)
    frame.transform(R)

# Reorient the mesh by aligning the frame with the world coordinate system.
# To do that, compute a frame-to-frame transformation,
# and apply it to the mesh and the frame.

world = ___

X = Transformation.from_frame_to_frame(___, ___)

mesh.transform(___)
frame.transform(___)

# Viz

viewer = App(width=1600, height=900)

viewer.view.camera.rz = 25
viewer.view.camera.rx = -65
viewer.view.camera.ty = -0.3
viewer.view.camera.tx = 0
viewer.view.camera.distance = 3

viewer.add(mesh, facecolors={left: (0, 0, 1), top: (1, 0, 0), front: (0, 1, 0)})
viewer.add(frame, linewidth=10)

viewer.show()

# Export

data['frame'] = ___

compas.json_dump(data, FILE_O)
