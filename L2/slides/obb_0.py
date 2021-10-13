from math import radians

from compas.geometry import Pointcloud, Box
from compas.geometry import Frame, Transformation, Rotation, Translation
from compas.geometry import bounding_box
from compas.numerical import pca_numpy

from compas_view2.app import App


pcl = Pointcloud.from_bounds(8, 5, 3, 100)

Rz = Rotation.from_axis_and_angle([0.0, 0.0, 1.0], radians(60))
Ry = Rotation.from_axis_and_angle([0.0, 1.0, 0.0], radians(20))
Rx = Rotation.from_axis_and_angle([1.0, 0.0, 0.0], radians(10))

T = Translation.from_vector([5.0, 8.0, 3.0])

pcl.transform(T * Rz * Ry * Rx)

point, axes, values = pca_numpy(pcl)

world = Frame.worldXY()
frame = Frame(point, axes[0], axes[1])

X = Transformation.from_frame_to_frame(frame, world)

pcl2 = pcl.transformed(X)
box2 = Box.from_bounding_box(bounding_box(pcl2))

box = box2.transformed(X.inverted())

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.ty = -2
viewer.view.camera.distance = 15

viewer.add(pcl, pointsize=5, color=(0, 0, 0))
viewer.add(frame)
viewer.add(pcl2, pointsize=5, color=(1, 0, 0))
viewer.add(box2, opacity=0.5)
viewer.add(box2.frame)
viewer.add(box, opacity=0.5)

viewer.show()
