from compas.datastructures import Mesh
from compas_plotters import Plotter

# generate a mesh grid from meshgrid
mesh = Mesh.from_meshgrid(nx=5, dx=2)

# choose a random edge sample from the mesh
start = mesh.edge_sample()[0]

# find edge strips
edges = mesh.edge_strip(start)

# find halfedge strips
# edges = mesh.halfedge_strip(start)

# find strip faces
faces = []
for u, v in edges:
    if mesh.halfedge_face(u, v) is not None:
        faces.append(mesh.halfedge_face(u, v))

# visualization edge settings
edgecolor = {}
edgewidth = {}
for edge in edges:
    edgecolor[edge] = (0, 1, 0)
    edgewidth[edge] = 2.0
edgecolor[start] = (1, 0, 0)

# visualization face settings
facecolor = {}
for face in faces:
    facecolor[face] = (1, 0.7, 0.7)

# plotter
plotter = Plotter()
artist = plotter.add(mesh,
                     edgecolor=edgecolor,
                     edgewidth=edgewidth,
                     sizepolicy='relative',
                     vertexsize=0.5,
                     )

# artist.draw_halfedges(halfedges = edges, color=edgecolor)
plotter.zoom_extents()
plotter.show()
