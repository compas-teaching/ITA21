import compas
from compas.geometry import Box, Scale
from compas_view2.app import App

# load the mesh data
mesh = compas.json_load('monkey.json')

# add a box
# and give the monkey some breathing room
box = Box.from_bounding_box(mesh.bounding_box())
box.transform(Scale.from_factors([1.5, 1.5, 1.5]))

# visualize the mesh and the box with the viewer
viewer = App()
viewer.add(mesh)
viewer.add(box, opacity=0.5)
viewer.show()

# export the moonkey in the box
compas.json_dump([mesh, box], 'monkey-in-box.json')
