import os
import compas
from compas.datastructures import Mesh
from compas.geometry import Box, Line, Transformation, Frame
from compas.geometry import oriented_bounding_box_numpy, scale_vector, add_vectors
from compas_view2.app import App
from compas_plotters import Plotter

# unserialize the block data
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'data', 'block.json')
mesh = Mesh.from_json(FILE)

# STEP 1: find the oriented bounding box
# hint1: "points = mesh.vertices_attributes('xyz', keys=mesh.vertices())" gives you all the points on the block
# hint2: oriented_bounding_box_numpy, Box.from_bounding_box
points = mesh.vertices_attributes('xyz', keys=mesh.vertices())
box = oriented_bounding_box_numpy(points)
box = Box.from_bounding_box(box)

# STEP 2: find the local frame of the bounding box
# hint: Box.frame
local_frame = box.frame

# Step 3: transform the bounding box from local frame to worldXY frame
# hint1: Frame.worldXY, Transformation.from_frame_to_frame, box.transformed(T)
# hint2: add the transformed bounding box to the viewer
world_frame = Frame.worldXY()
T = Transformation.from_frame_to_frame(local_frame, world_frame)
box_T = box.transformed(T)

# STEP 4: draw the xyz-axes of the local frame, worldXY frame
# hint1: Frame.xaxis, Line, scale_vector
# hint2: add the lines to the viewer
local_xaxis = scale_vector(local_frame.xaxis, box.xsize)
local_xline = Line(local_frame.point, add_vectors(
    local_frame.point, local_xaxis))
local_yaxis = scale_vector(local_frame.yaxis, box.ysize)
local_yline = Line(local_frame.point, add_vectors(
    local_frame.point, local_yaxis))
local_zaxis = scale_vector(local_frame.zaxis, box.zsize)
local_zline = Line(local_frame.point, add_vectors(
    local_frame.point, local_zaxis))

world_xline = local_xline.transformed(T)
world_yline = local_yline.transformed(T)
world_zline = local_zline.transformed(T)

# Step 5: transform the block using the same transformation
# hint1: mesh.transformed(T)
# hint2: add the transformed block to the viewer
mesh_T = mesh.transformed(T)

# visualization
viewer = App()
viewer.add(mesh)
viewer.add(box, show_faces=False, show_edges=True)
viewer.add(local_xline, linewidth=3, linecolor=(0, 1, 0))
viewer.add(local_yline, linewidth=3, linecolor=(0, 0, 1))
viewer.add(local_zline, linewidth=3, linecolor=(1, 0, 0))

viewer.add(mesh_T)
viewer.add(box_T, show_faces=False, show_edges=True)
viewer.add(world_xline, linewidth=3, linecolor=(0, 1, 0))
viewer.add(world_yline, linewidth=3, linecolor=(0, 0, 1))
viewer.add(world_zline, linewidth=3, linecolor=(1, 0, 0))

viewer.run()
