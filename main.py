from shapes import Circle, Rectangle
from solids import Sphere, Cube

# Circle example
circle = Circle(radius=5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

# Sphere example
sphere = Sphere(radius=5)
print(f"Sphere Volume: {sphere.volume()}")
print(f"Sphere Surface Area: {sphere.surface_area()}")
