import compas
from compas_view2.app import App

mesh = compas.json_load('L5/tubemesh.json')

viewer = App(width=1600, height=900)

viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.tx = 0
viewer.view.camera.ty = 0
viewer.view.camera.distance = 12

viewer.add(mesh)

viewer.show()
