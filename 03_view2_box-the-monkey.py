import compas
from compas.geometry import Box, Scale
from compas_view2.app import App

mesh = compas.json_load('monkey.json')

box = Box.from_bounding_box(mesh.bounding_box())
box.transform(Scale.from_factors([1.5, 1.5, 1.5]))

viewer = App()
viewer.add(mesh)
viewer.add(box, opacity=0.5)
viewer.show()

compas.json_dump([mesh, box], 'monkey-in-box.json')
