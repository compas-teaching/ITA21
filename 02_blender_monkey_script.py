import bpy
import bmesh
import compas
import compas_blender
from compas.datastructures import Mesh
from compas_blender.artists import MeshArtist

# clear all objects from the current scene
compas_blender.clear()

# create the monkey bmesh
bm = bmesh.new()
bmesh.ops.create_monkey(bm)

# convert the bmesh to a blender mesh data block
# (this is just how blender works)
meshdata = bpy.data.meshes.new('Mesh')
bm.to_mesh(meshdata)
bm.free()

# get the vertices and the faces of the blender mesh
# (in the future we will use a COMPAS function for this)
vertices = [list(vertex.co) for vertex in meshdata.vertices]
faces = [list(face.vertices) for face in meshdata.polygons]

# make a COMPAS mesh from vertices and faces
mesh = Mesh.from_vertices_and_faces(vertices, faces)

# optional: subdivide
mesh = mesh.subdivide(k=3)

# use an artist to visualize the mesh
artist = MeshArtist(mesh)
artist.draw_mesh()

# export the mesh to JSON
compas.json_dump(mesh, '/Users/vanmelet/Code/ITA21/monkey.json')
