from dimencalc.shapes import Circle, Rectangle, Square, Triangle, Parallelogram, Trapezoid, Ellipse, Pentagon, Hexagon, Rhombus

# Testing Circle
circle = Circle(5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

# Testing Rectangle
rectangle = Rectangle(10, 5)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

# Testing Square
square = Square(6)
print(f"Square Area: {square.area()}")
print(f"Square Perimeter: {square.perimeter()}")

# Testing Triangle
triangle = Triangle(3, 4, 5)
print(f"Triangle Area: {triangle.area()}")
print(f"Triangle Perimeter: {triangle.perimeter()}")

# Testing Parallelogram
parallelogram = Parallelogram(8, 4)
print(f"Parallelogram Area: {parallelogram.area()}")
print(f"Parallelogram Perimeter: {parallelogram.perimeter(6)}")

# Testing Trapezoid
trapezoid = Trapezoid(7, 5, 4)
print(f"Trapezoid Area: {trapezoid.area()}")
print(f"Trapezoid Perimeter: {trapezoid.perimeter(6, 7)}")

# Testing Ellipse
ellipse = Ellipse(5, 3)
print(f"Ellipse Area: {ellipse.area()}")
print(f"Ellipse Perimeter: {ellipse.perimeter()}")

# Testing Pentagon
pentagon = Pentagon(7)
print(f"Pentagon Area: {pentagon.area()}")
print(f"Pentagon Perimeter: {pentagon.perimeter()}")

# Testing Hexagon
hexagon = Hexagon(10)
print(f"Hexagon Area: {hexagon.area()}")
print(f"Hexagon Perimeter: {hexagon.perimeter()}")

# Testing Rhombus
rhombus = Rhombus(6, 8)
print(f"Rhombus Area: {rhombus.area()}")
print(f"Rhombus Perimeter: {rhombus.perimeter(5)}")
