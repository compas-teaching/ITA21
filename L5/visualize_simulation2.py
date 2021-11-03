import os
import math as m
import compas
from compas.datastructures import Mesh
from compas.geometry import matrix_from_axis_and_angle
from compas_view2.app import App

# output folder
folder = os.path.abspath("//Users//duch//Documents//PhD//ita21_materials//simulation")
data = compas.json_load(os.path.join(folder, 'data.json'))

mesh = data['mesh']

viewer = App(width=1200, height=750)
vertices = data['frames'][0]
for vertex in mesh.vertices():
    mesh.vertex_attributes(vertex, 'xyz', vertices[vertex])
meshobj = viewer.add(mesh)

@viewer.on(interval=100, frames=len(data['frames']))
def animate(i):
    vertices = data['frames'][i]
    for vertex in mesh.vertices():
        mesh.vertex_attributes(vertex, 'xyz', vertices[vertex])
    meshobj.update()

viewer.show()
