import random
from compas.geometry import Pointcloud, Sphere
from compas.utilities import i_to_red
from compas_view2.app import App

viewer = App()

for point in Pointcloud.from_bounds(8, 5, 5 * 5 / 8, 53):
    radius = random.random()
    sphere = Sphere(point, 0.5 * radius)

    viewer.add(sphere,
               color=i_to_red(radius, normalize=True))

viewer.show()
