import os

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

VERTEX = 2

vertices = mesh.vertex_neighbors(VERTEX, ordered=True)
faces = mesh.vertex_faces(VERTEX, ordered=True)

halfedges = [
    (VERTEX, vertices[0]),
    (vertices[0], VERTEX),
    (VERTEX, vertices[1]),
    (vertices[1], VERTEX),
    (VERTEX, vertices[2]),
    (vertices[2], VERTEX),
    (VERTEX, vertices[3]),
    (vertices[3], VERTEX),
]

halfedge_color = {
    halfedges[0]: (0, 0, 0,),
    halfedges[2]: (0, 0, 0,),
    halfedges[4]: (0, 0, 0,),
    halfedges[6]: (0, 0, 0,)
}

vertex_color = {
    VERTEX: (1.0, 0.0, 0.0),
}

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexcolor=vertex_color)

meshartist.draw_halfedges(halfedges=halfedges, color=halfedge_color)
meshartist.draw_vertexlabels(text={vertex: f'{index}' for index, vertex in enumerate(vertices)})
meshartist.draw_facelabels(text={face: f'{index}' for index, face in enumerate(faces)})

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
