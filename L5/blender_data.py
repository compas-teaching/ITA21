import os
import bpy
import bmesh
import compas
from compas.datastructures import Mesh

# scene
bpyscene = bpy.context.scene

# output folder
folder = os.path.abspath(
    "//Users//duch//Documents//PhD//ita21_materials//simulation")

# load blender mesh data from a blender object
meshobj = bpy.context.scene.objects['Cube']
meshdata = bpy.data.meshes.new_from_object(meshobj)

# get the vertices and the faces of the blender mesh
# (in the future we will use a COMPAS function for this)
vertices = [list(vertex.co) for vertex in meshdata.vertices]
faces = [list(face.vertices) for face in meshdata.polygons]
# make a COMPAS mesh from vertices and faces
mesh = Mesh.from_vertices_and_faces(vertices, faces)

# data
data = {'mesh': mesh, 'frames': []}

# frames start, end
frame_start = bpy.data.scenes["Scene"].frame_start
frame_end = bpy.data.scenes["Scene"].frame_end

# output every 5 frames
for f in range(frame_start, frame_end):
    if f % 5 == 0:
        # set the scene to the frame
        print('Running frame {}'.format(f))
        bpyscene.frame_set(f)

        # Get the dependency graph state for this frame
        dg = bpy.context.evaluated_depsgraph_get()
        # set output object to the cube
        ob = bpy.context.scene.objects['Cube']
        # The mesh from the object and dependency graph
        me = ob.data
        bm = bmesh.new()
        bm.from_object(ob, dg)
        bm.to_mesh(me)
        # mesh vertex coordinate of current frame
        vertices = [list(vertex.co) for vertex in bm.verts]
        # save the vertices to data
        data['frames'].append(vertices)
        bm.free()

compas.json_dump(data, os.path.join(folder, 'data.json'))
