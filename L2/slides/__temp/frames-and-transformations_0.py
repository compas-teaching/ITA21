from compas.geometry import Point
from compas_view2.app import App

a = Point(0, 0, 0)
b = Point(1, 1, 1)
c = Point(0, 1, 0)

viewer = App(width=800, height=900)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -75
viewer.view.camera.distance = 5

viewer.add(a, size=10, color=(1, 0, 0))
viewer.add(b, size=10, color=(0, 1, 0))
viewer.add(c, size=10, color=(0, 0, 1))

viewer.show()
