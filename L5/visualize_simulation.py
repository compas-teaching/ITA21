import os
from compas.datastructures import Mesh
from compas.datastructures import mesh_transform_numpy
from compas.geometry import matrix_from_axis_and_angle
from compas_view2.app import App

# output folder
folder = os.path.abspath("//Users//duch//Documents//PhD//ita21_materials//simulation")
files = [ob for ob in os.listdir(folder) if ob.endswith(".obj")]
files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
file_len = len(files)
print(files[0])

T = matrix_from_axis_and_angle([0, 0.5, 0.3], m.pi / 4)

FILE_I = os.path.join(folder, files[0])
mesh = Mesh.from_obj(FILE_I)
mesh_transform_numpy(mesh, T)

viewer = App(width=1200, height=750)
# viewer.view.camera.rz = 90
# viewer.view.camera.rx = -75
# viewer.view.camera.tx = 0
# viewer.view.camera.ty = -1
# viewer.view.camera.distance = 6

meshobj = viewer.add(mesh)

@viewer.on(interval=100, frames=file_len)
def move(f):
    FILE_I = os.path.join(folder, files[f])
    mesh = Mesh.from_obj(FILE_I)
    # meshobj.vertices = [mesh.vertex_xyz[vkey] for vkey in mesh.vertice()]
    # mesh
    viewer.add(mesh)

viewer.show()
