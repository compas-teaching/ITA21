from compas.geometry import Point, Line
from compas_view2.app import App

a = Point(0, 0, 0)
b = Point(1, 1, 1)
c = Point(0, 1, 0)

x = (b - a).unitized()
y = (c - a).unitized()
z = x.cross(y).unitized()

print(x.length)
print(y.length)
print(z.length)

print(x.dot(y))
print(y.dot(z))
print(z.dot(x))

viewer = App(width=800, height=900)
viewer.view.camera.rz = 0
viewer.view.camera.rx = -75
viewer.view.camera.distance = 5

viewer.add(a, size=10, color=(1, 0, 0))
viewer.add(b, size=10, color=(0, 1, 0))
viewer.add(c, size=10, color=(0, 0, 1))

viewer.add(Line(a, a + x), linewidth=3)
viewer.add(Line(a, a + y), linewidth=3)
viewer.add(Line(a, a + z), linewidth=3)

viewer.show()
