import os
from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

edge_width = {(1, 2): 3.0}
vertex_color = {2: (1, 0, 0), 1: (1.0, 0.7, 0.7)}

nbrs = mesh.vertex_neighbors(2, ordered=True)
i = nbrs.index(1)

nbrs = nbrs[i:] + nbrs[:i]

vertex_text = {1: 'i'}
for index, nbr in enumerate(nbrs[1:][::-1]):
    vertex_text[nbr] = f'-{index + 1}'

meshartist = plotter.add(mesh, sizepolicy='absolute', edgewidth=edge_width, vertexcolor=vertex_color)

meshartist.draw_vertexlabels(text=vertex_text)

plotter.zoom_extents()
# plotter.show()

plotter.save(f'L3/images/{os.path.basename(__file__)}.png', dpi=150)
