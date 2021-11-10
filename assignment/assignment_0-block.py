import os
import compas
from compas.geometry import Box
from compas.geometry import Plane, Circle, Cone
from compas.geometry import boolean_difference_mesh_mesh
from compas.geometry import Polyhedron
from compas.geometry import is_coplanar, is_colinear

from compas.datastructures import Mesh
from compas.datastructures import mesh_weld

from compas_view2.app import App

# Input

HERE = os.path.join(os.path.expanduser('~'), 'Code/ITA21/L5')
FILE = os.path.join(HERE, "assignment_0.json")

# Make a box

box = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1.5)

# Make a cone

cone = Cone(Circle(Plane([1, 0, 0], [0, 0, 1]), 0.7), 4)

# Compute the boolean difference of the box and the cone

A = ___.to_vertices_and_faces(triangulated=True)
B = ___.to_vertices_and_faces(u=64, triangulated=True)
C = boolean_difference_mesh_mesh(___)

shape = Polyhedron(___)

# Convert to mesh

mesh = ___

# Clean up by welding all vertices

mesh = mesh_weld(mesh)

# Merge all coplanar faces

while True:
    merge = []
    for face in mesh.faces():
        points = mesh.face_coordinates(face)
        nbrs = mesh.face_neighbors(face)
        for nbr in nbrs:
            if is_coplanar(points + mesh.face_coordinates(nbr), tol=1e-12):
                merge = [face, nbr]
                break
        if merge:
            break
    if not merge:
        break
    mesh.merge_faces(merge)
    
# Merge all colinear edges

while True:
    collapse = []
    for face in mesh.faces():
        for u, v, w in mesh.face_corners(face):
            a = mesh.vertex_coordinates(u)
            b = mesh.vertex_coordinates(v)
            c = mesh.vertex_coordinates(w)
            if is_colinear(a, b, c, tol=1e-12):
                collapse = [u, v]
                break
        if collapse:
            break
    if not collapse:
        break
    u, v = collapse
    mesh.collapse_edge(u, v, t=0.0, allow_boundary=True)

# Viz

viewer = App(width=1600, height=900)

viewer.view.camera.ty = -0.8
viewer.view.camera.tx = -0.7
viewer.view.camera.distance = 3

viewer.add(mesh, show_vertices=True)
viewer.show()

# Output

data = {'shape': ___, 'mesh': ___}

compas.json_dump(data, FILE)
