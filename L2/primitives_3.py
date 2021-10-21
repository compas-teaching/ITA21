from compas.geometry import Pointcloud, Translation
from compas.geometry import Polygon
from compas.utilities import i_to_black, is_color_light
from compas_plotters import Plotter

plotter = Plotter(figsize=(16, 9), zstack='natural')

N = 13
cloud = Pointcloud.from_bounds(x=16, y=9, z=0, n=N)

for index, point in enumerate(cloud):
    n = index + 3
    radius = (index + 1) / N

    color1 = i_to_black((index + 1) / N, normalize=True)
    color2 = i_to_black(1 - (index + 1) / N, normalize=True)
    facecolor = color1 if is_color_light(color1) else color2
    edgecolor = color2 if is_color_light(color1) else color1

    polygon = Polygon.from_sides_and_radius_xy(n=n, radius=radius)
    polygon.transform(Translation.from_vector(point))

    plotter.add(polygon,
                facecolor=facecolor,
                edgecolor=edgecolor,
                alpha=0.7)

plotter.zoom_extents()
plotter.show()