import math

# shapes.py

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def radius_from_area(self, area):
        """Calculate radius from the area."""
        return (area / 3.14159) ** 0.5

    def radius_from_perimeter(self, perimeter):
        """Calculate radius from the perimeter."""
        return perimeter / (2 * 3.14159)



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def length_from_area(self, area, width):
        """Calculate length from the area and width."""
        return area / width

    def width_from_area(self, area, length):
        """Calculate width from the area and length."""
        return area / length

    def length_from_perimeter(self, perimeter, width):
        """Calculate length from the perimeter and width."""
        return (perimeter / 2) - width

    def width_from_perimeter(self, perimeter, length):
        """Calculate width from the perimeter and length."""
        return (perimeter / 2) - length

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

    def side_from_area(self, area):
        """Calculate side length from the area."""
        return area ** 0.5

    def side_from_perimeter(self, perimeter):
        """Calculate side length from the perimeter."""
        return perimeter / 4


class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # Side length a
        self.b = b  # Side length b
        self.c = c  # Side length c

    def perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.a + self.b + self.c

    def area(self):
        """Calculate the area of the triangle using Heron's formula."""
        s = self.perimeter() / 2  # Semi-perimeter
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def angles(self):
        """Calculate angles of the triangle in degrees."""
        A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = 180 - A - B
        return A, B, C

    @staticmethod
    def side_from_area(area, base, height):
        """Calculate side length from the area and base."""
        return 2 * area / base

    @staticmethod
    def side_from_perimeter(perimeter, a, b):
        """Calculate the third side from the perimeter and two other sides."""
        return perimeter - (a + b)


class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Calculate the area of the parallelogram."""
        return self.base * self.height

    def perimeter(self, side_length):
        """Calculate the perimeter of the parallelogram."""
        return 2 * (self.base + side_length)

    def angles(self, side_length):
        """Calculate angles of the parallelogram in degrees."""
        angle_A = math.degrees(math.acos((self.base**2 + side_length**2 - self.height**2) / (2 * self.base * side_length)))
        angle_B = 180 - angle_A
        return angle_A, angle_B

    @staticmethod
    def side_from_area(area, base):
        """Calculate side length using area and base."""
        return area / base

    @staticmethod
    def base_from_perimeter(perimeter, side_length):
        """Calculate base using perimeter and side length."""
        return (perimeter / 2) - side_length



class Trapezoid:
    def __init__(self, a, b, height):
        self.a = a  # Length of base a
        self.b = b  # Length of base b
        self.height = height

    def area(self):
        """Calculate the area of the trapezoid."""
        return 0.5 * (self.a + self.b) * self.height

    def perimeter(self, side_c, side_d):
        """Calculate the perimeter of the trapezoid."""
        return self.a + self.b + side_c + side_d

    def angles(self, side_c, side_d):
        """Calculate angles of the trapezoid in degrees."""
        angle_A = math.degrees(math.atan(self.height / ((self.b - self.a) / 2)))  # angle at base a
        angle_B = 180 - angle_A  # angle at base b
        return angle_A, angle_B

    @staticmethod
    def base_from_area(area, base_a, base_b):
        """Calculate the height from area and two bases."""
        return (2 * area) / (base_a + base_b)

    @staticmethod
    def side_from_perimeter(perimeter, base_a, base_b):
        """Calculate the sum of the non-parallel sides from the perimeter."""
        return perimeter - (base_a + base_b)



import math

class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def area(self):
        """Calculate the area of the ellipse."""
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def perimeter(self):
        """Approximate the perimeter of the ellipse using Ramanujan's formula."""
        return math.pi * (3 * (self.semi_major_axis + self.semi_minor_axis) -
                          math.sqrt((3 * self.semi_major_axis + self.semi_minor_axis) * 
                                     (self.semi_major_axis + 3 * self.semi_minor_axis)))

    @staticmethod
    def semi_major_from_area(area, semi_minor_axis):
        """Calculate semi-major axis from area and semi-minor axis."""
        return area / (math.pi * semi_minor_axis)

    @staticmethod
    def semi_minor_from_area(area, semi_major_axis):
        """Calculate semi-minor axis from area and semi-major axis."""
        return area / (math.pi * semi_major_axis)


class Pentagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculate the area of the regular pentagon."""
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))

    def perimeter(self):
        """Calculate the perimeter of the pentagon."""
        return 5 * self.side

    def angles(self):
        """Calculate angles of the regular pentagon in degrees."""
        return 108  # All angles are equal in a regular pentagon

    @staticmethod
    def side_from_area(area):
        """Calculate side length from area."""
        return math.sqrt((4 * area) / (5 * math.tan(math.pi / 5)))


class Hexagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculate the area of the regular hexagon."""
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def perimeter(self):
        """Calculate the perimeter of the hexagon."""
        return 6 * self.side

    def angles(self):
        """Calculate angles of the regular hexagon in degrees."""
        return 120  # All angles are equal in a regular hexagon

    @staticmethod
    def side_from_area(area):
        """Calculate side length from area."""
        return math.sqrt((2 * area) / (3 * math.sqrt(3)))



class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        """Calculate the area of the rhombus."""
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self, side):
        """Calculate the perimeter of the rhombus."""
        return 4 * side

    def angles(self, side):
        """Calculate angles of the rhombus using diagonals."""
        angle_A = math.degrees(math.atan(self.diagonal2 / self.diagonal1))
        angle_B = 180 - angle_A
        return angle_A, angle_B

    @staticmethod
    def side_from_area(area, diagonal1):
        """Calculate side length from area and one diagonal."""
        return (2 * area) / diagonal1

    @staticmethod
    def diagonal1_from_area(area, diagonal2):
        """Calculate first diagonal length from area and second diagonal."""
        return (2 * area) / diagonal2
