import os
import bpy
import bmesh
import compas
import compas_blender
from compas.datastructures import Mesh
from compas_blender.artists import MeshArtist


class BlenderMesh:

    def __init__(self, mesh):
        self.mesh = mesh

    @classmethod
    def from_object(cls, obj):
        mesh = bpy.data.meshes.new_from_object(obj)
        return cls(mesh)

    @classmethod
    def from_bmesh(cls, bmesh, free=True):
        mesh = bpy.data.meshes.new('Mesh')
        bmesh.to_mesh(mesh)
        if free:
            bmesh.free()
        return cls(mesh)

    @classmethod
    def from_monkey(cls):
        bm = bmesh.new()
        bmesh.ops.create_monkey(bm)
        mesh = bpy.data.meshes.new('Mesh')
        bm.to_mesh(mesh)
        bm.free()
        return cls(mesh)

    @property    
    def vertices(self):
        return [list(vertex.co) for vertex in self.mesh.vertices]

    @property
    def faces(self):
        return [list(face.vertices) for face in self.mesh.polygons]

    def to_compas(self, cls=None):
        from compas.datastructures import Mesh
        cls = cls or Mesh
        return cls.from_vertices_and_faces(self.vertices, self.faces)


# clear all objects from the current scene
compas_blender.clear()

mesh = BlenderMesh.from_monkey().to_compas()

# optional: subdivide
mesh = mesh.subdivide(k=2)

# use an artist to visualize the mesh
artist = MeshArtist(mesh)
artist.draw_mesh()

# export the mesh to JSON
compas.json_dump(mesh, os.path.expanduser('~/Code/ITA21/monkey.json'))
