from compas.geometry import Point, Vector, Frame
from compas_view2.app import App

world = Frame.worldXY()

viewer = App(width=800, height=900)
viewer.view.camera.rz = -30
viewer.view.camera.rx = -60
viewer.view.camera.tx = -2
viewer.view.camera.distance = 8

viewer.add(world, linewidth=5)

viewer.show()
