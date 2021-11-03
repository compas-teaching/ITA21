import os
import compas
from compas_view2.app import App

# load data
here = os.path.dirname(__file__)
file = os.path.join(here, 'blender_data.json')
data = compas.json_load(file)
mesh = data['mesh']

# initiate the viewer
# add the mesh to the viewer
viewer = App(width=1200, height=750)
meshobj = viewer.add(mesh)

# animation
@viewer.on(interval=100, frames=len(data['frames']))
def animate(i):
    vertices = data['frames'][i]
    for vertex in mesh.vertices():
        mesh.vertex_attributes(vertex, 'xyz', vertices[vertex])
    meshobj.update()
    
# launch the viewer
viewer.show()