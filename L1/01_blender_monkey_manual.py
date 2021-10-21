import bpy
import compas
import os
from compas.datastructures import Mesh

# load blender mesh data from a blender object
meshobj = bpy.context.scene.objects['Suzanne']
meshdata = bpy.data.meshes.new_from_object(meshobj)

# get the vertices and the faces of the blender mesh
# (in the future we will use a COMPAS function for this)
vertices = [list(vertex.co) for vertex in meshdata.vertices]
faces = [list(face.vertices) for face in meshdata.polygons]

# make a COMPAS mesh from vertices and faces
mesh = Mesh.from_vertices_and_faces(vertices, faces)

# export the mesh to JSON
compas.json_dump(mesh, os.path.expanduser('~/Code/ITA21/L1/monkey.json'))
