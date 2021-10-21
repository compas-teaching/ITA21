from math import radians

from compas.geometry import Pointcloud, Box, Point, Vector, Line
from compas.geometry import Frame, Transformation, Rotation, Translation
from compas.geometry import bounding_box, closest_point_on_line
from compas.numerical import pca_numpy

from compas_view2.app import App
from compas_view2.objects import Collection


pcl = Pointcloud.from_bounds(8, 5, 3, 100)

Rz = Rotation.from_axis_and_angle([0.0, 0.0, 1.0], radians(60))
Ry = Rotation.from_axis_and_angle([0.0, 1.0, 0.0], radians(20))
Rx = Rotation.from_axis_and_angle([1.0, 0.0, 0.0], radians(10))

T = Translation.from_vector([5.0, 8.0, 3.0])

pcl.transform(T * Rz * Ry * Rx)

point, axes, _ = pca_numpy(pcl)

# point = Point(*point)
# xaxis = Vector(*axes[0])
# yaxis = Vector(*axes[1])

world = Frame.worldXY()
frame = Frame(point, axes[0], axes[1])

X = Transformation.from_frame_to_frame(frame, world)

pcl2 = pcl.transformed(X)
box2 = Box.from_bounding_box(bounding_box(pcl2))

box = box2.transformed(X.inverted())

# line_x = Line(point - xaxis.scaled(5), point + xaxis.scaled(5))
# line_y = Line(point - yaxis.scaled(5), point + yaxis.scaled(5))

# points_x = [Point(* closest_point_on_line(point, line_x)) for point in pcl]
# points_y = [Point(* closest_point_on_line(point, line_y)) for point in pcl]

viewer = App(width=1200, height=750)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.ty = -2
viewer.view.camera.distance = 15

viewer.add(pcl, pointsize=10)
viewer.add(pcl2, pointsize=10)
viewer.add(frame)
viewer.add(box2, show_faces=False, linewidth=3)
viewer.add(box, opacity=0.5)

# viewer.add(line_x, color=(1, 0, 0))
# viewer.add(line_y, color=(0, 1, 0))

# viewer.add(Collection(points_x), pointcolor=(1, 0, 0))
# viewer.add(Collection(points_y), pointcolor=(0, 1, 0))

viewer.show()
