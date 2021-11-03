import os
import compas
from compas_view2.app import App

here = os.path.dirname(__file__)
path = os.path.join(here, 'tubemesh.json')

mesh = compas.json_load(path)

viewer = App(width=1600, height=900)

viewer.view.camera.rz = 0
viewer.view.camera.rx = -65
viewer.view.camera.tx = 0
viewer.view.camera.ty = 0
viewer.view.camera.distance = 12

viewer.add(mesh)

viewer.show()
