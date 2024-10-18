# dimencalc Library User Guide

The dimencalc library provides easy-to-use functions for calculating the area, perimeter, and volume of a variety of 2D and 3D geometric shapes. You can also compute side lengths, radii, heights, and other dimensions based on these properties.

## Installation

For now, you can copy the `shapes.py` file into your project directory. Once you have packaged the library, users will be able to install it via pip.

```pip install dimencalc```

## Getting Started

To use the library, start by importing the relevant classes for the shape you want to calculate properties for.

```
from dimencalc.shapes import Circle, Rectangle, Triangle
from dimencalc.solids import Sphere, Cube, Cylinder

# Alternatively, to import everything in one go:
from dimencalc.shapes import *
from dimencalc.solids import *
```

## 2D Shapes Usage

### Circle
Calculate the area, perimeter (circumference), and other related properties of a circle.

```python
circle = Circle(radius=5)
area = circle.area()
perimeter = circle.perimeter()

# Reverse calculations
radius_from_area = circle.radius_from_area(area)
radius_from_perimeter = circle.radius_from_perimeter(perimeter)
```

### Rectangle
Calculate the area and perimeter of a rectangle, or calculate a missing side from area or perimeter.

```python
rectangle = Rectangle(length=10, width=5)
area = rectangle.area()
perimeter = rectangle.perimeter()

# Reverse calculations
length_from_area = rectangle.length_from_area(area, width=5)
width_from_perimeter = rectangle.width_from_perimeter(perimeter, length=10)
```

### Square
Works similarly to the rectangle but operates on a single side.

```python
square = Square(side_length=4)
area = square.area()
perimeter = square.perimeter()

# Reverse calculations
side_from_area = square.side_from_area(area)
side_from_perimeter = square.side_from_perimeter(perimeter)
```

### Triangle
For triangles, you can calculate the area using Heron’s formula.

```python
triangle = Triangle(a=3, b=4, c=5)
area = triangle.area()
perimeter = triangle.perimeter()
angles = triangle.angles()
```

### Pentagon & Hexagon
Calculate properties of regular pentagons and hexagons.

```python
pentagon = Pentagon(side=6)
hexagon = Hexagon(side=6)

pentagon_area = pentagon.area()
hexagon_area = hexagon.area()
```

## 3D Shapes Usage

### Sphere
For spheres, you can calculate both volume and surface area.

```python
sphere = Sphere(radius=5)
volume = sphere.volume()
surface_area = sphere.surface_area()

# Reverse calculations
radius_from_volume = sphere.radius_from_volume(volume)
radius_from_surface_area = sphere.radius_from_surface_area(surface_area)
```

### Cylinder
Calculate the volume and surface area of a cylinder.

```python
cylinder = Cylinder(radius=3, height=7)
volume = cylinder.volume()
surface_area = cylinder.surface_area()

# Reverse calculations
radius_from_volume = cylinder.radius_from_volume(volume)
height_from_volume = cylinder.height_from_volume(volume)
```

### Cube
Calculate the volume and surface area for a cube.

```python
cube = Cube(side_length=4)
volume = cube.volume()
surface_area = cube.surface_area()

# Reverse calculations
side_from_volume = cube.side_from_volume(volume)
side_from_surface_area = cube.side_from_surface_area(surface_area)
```

### Rectangular Prism (Cuboid)

```python
cuboid = Cuboid(length=5, width=4, height=3)
volume = cuboid.volume()
surface_area = cuboid.surface_area()

# Reverse calculations
length_from_volume = cuboid.length_from_volume(volume, width=4, height=3)
width_from_volume = cuboid.width_from_volume(volume, length=5, height=3)
```

### Cone
Calculate the volume and surface area of a cone.

```python
cone = Cone(radius=3, height=5)
volume = cone.volume()
surface_area = cone.surface_area()
```

## More Complex Shapes

### Frustum
Calculate the volume and surface area of a truncated cone (frustum).

```python
frustum = Frustum(radius_top=4, radius_bottom=6, height=8)
volume = frustum.volume()
surface_area = frustum.surface_area()
```

### Torus
For a torus (doughnut shape):

```python
torus = Torus(major_radius=6, minor_radius=2)
volume = torus.volume()
surface_area = torus.surface_area()
```

### Ellipsoids, Parallelograms, Rhombuses, and More
For other shapes like ellipsoids, rhombuses, octahedrons, etc., you can refer to the corresponding classes in the library and use similar methods to calculate dimensions based on the properties provided.

```python
ellipse = Ellipse(semi_major_axis=6, semi_minor_axis=4)
ellipse_area = ellipse.area()
ellipse_perimeter = ellipse.perimeter()
```

## Reversing Calculations

In addition to calculating area, perimeter, and volume, dimencalc also supports reverse calculations like:

- Calculating the radius from the area of a circle.
- Finding the side length of a cube from the volume.
- Determining the height of a cylinder based on volume.

### Example:

```python
# Reverse calculation for a cube
cube = Cube(side_length=4)
volume = cube.volume()
side_length = cube.side_from_volume(volume)  # Get side length from volume
```

## Conclusion

The dimencalc library provides a clean and structured approach to working with geometric shapes and objects. Each shape comes with methods for standard geometric calculations, as well as reverse methods to deduce properties from given values like volume, area, or perimeter.

This guide should help you get started with the library. You can extend it by adding more shapes or complex geometries as needed.
```

Feel free to make any further adjustments!
