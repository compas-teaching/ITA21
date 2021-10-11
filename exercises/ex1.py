import os
from compas.datastructures import Mesh
from compas_view2.app import App

# unserialize the block data
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'data', 'block.json')
mesh = Mesh.from_json(FILE)

# STEP 1: find the oriented bounding box
# hint1: "points = mesh.vertices_attributes('xyz', keys=mesh.vertices())" gives you all the points coordinates on the block
# hint2: oriented_bounding_box_numpy, Box.from_bounding_box

# STEP 2: find the local frame of the bounding box
# hint: Box.frame

# Step 3: transform the bounding box from local frame to worldXY frame
# hint1: Frame.worldXY, Transformation.from_frame_to_frame, box.transformed(T)
# hint2: add the transformed bounding box to the viewer

# STEP 4: draw the xyz-axes of the local frame, worldXY frame
# hint1: Frame.xaxis, Line, scale_vector
# hint2: add the lines to the viewer

# Step 5: transform the block using the same transformation
# hint1: mesh.transformed(T)
# hint2: add the transformed block to the viewer

# visualization
viewer = App()
viewer.add(mesh)
viewer.run()