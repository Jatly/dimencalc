from dimencalc.solids import Cuboid, Sphere, Cylinder, Cone, Pyramid, RectangularPrism, Torus

# Testing Cuboid
cuboid = Cuboid(5, 4, 3)
print(f"Cuboid Volume: {cuboid.volume()}")
print(f"Cuboid Surface Area: {cuboid.surface_area()}")

# Testing Sphere
sphere = Sphere(6)
print(f"Sphere Volume: {sphere.volume()}")
print(f"Sphere Surface Area: {sphere.surface_area()}")

# Testing Cylinder
cylinder = Cylinder(5, 10)
print(f"Cylinder Volume: {cylinder.volume()}")
print(f"Cylinder Surface Area: {cylinder.surface_area()}")

# Testing Cone
cone = Cone(4, 9)
print(f"Cone Volume: {cone.volume()}")
print(f"Cone Surface Area: {cone.surface_area()}")

# Testing Pyramid

# Create a pyramid with base area = 6 and height = 8
pyramid = Pyramid(6, 8)

# Calculate volume
print(f"Pyramid Volume: {pyramid.volume()}")

# Calculate surface area with base perimeter = 10 and slant height = 12
print(f"Pyramid Surface Area: {pyramid.surface_area(10, 12)}")

# Testing Prism
prism = RectangularPrism(6, 5, 8)
print(f"Prism Volume: {prism.volume()}")
print(f"Prism Surface Area: {prism.surface_area()}")

# Testing Torus
torus = Torus(8, 3)
print(f"Torus Volume: {torus.volume()}")
print(f"Torus Surface Area: {torus.surface_area()}")
