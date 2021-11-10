import os
import compas

from compas.geometry import Frame, Box
from compas.geometry import Scale
from compas.datastructures import Mesh

from compas_view2.app import App

# I/O

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE_I = os.path.join(HERE, "assignment_2.json")
FILE_O = os.path.join(HERE, "assignment_3.json")

# Load data

data = compas.json_load(FILE_I)

mesh: Mesh = ___
frame: Frame = ___

# Compute the bounding box of the mesh.
# And convert it into a box geometry object.

bbox = mesh.___()
blank = Box.from_bounding_box(___)

# Add some padding to the blank,
# by scaling it by 10% in all directions.
# Use the frame of the blank as basis for the scaling.

blank.transform(Scale.from_factors([___, ___, ___], frame=___))

# Viz

viewer = App(width=1600, height=900)

viewer.view.camera.rz = 70
viewer.view.camera.rx = -70
viewer.view.camera.ty = -0.3
viewer.view.camera.tx = 0
viewer.view.camera.distance = 3

viewer.add(mesh, show_faces=False)
viewer.add(blank, opacity=0.5)
viewer.add(blank.frame, linewidth=10)
viewer.show()

# Export

data['blank'] = ___

compas.json_dump(data, FILE_O)
