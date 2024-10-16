import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        """Calculate the volume of the sphere."""
        return (4/3) * math.pi * self.radius ** 3

    def surface_area(self):
        """Calculate the surface area of the sphere."""
        return 4 * math.pi * self.radius ** 2

    def radius_from_volume(self, volume):
        """Calculate radius from the volume."""
        return ((3 * volume) / (4 * math.pi)) ** (1/3)

    def radius_from_surface_area(self, surface_area):
        """Calculate radius from surface area."""
        return (surface_area / (4 * math.pi)) ** 0.5



class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        """Calculate the volume of the cylinder."""
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        """Calculate the surface area of the cylinder."""
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def radius_from_volume(self, volume):
        """Calculate radius from volume and height."""
        return ((volume / (math.pi * self.height)) ** (1/2))

    def height_from_volume(self, volume):
        """Calculate height from volume and radius."""
        return volume / (math.pi * self.radius ** 2)


class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        """Calculate the volume of the cone."""
        return (1/3) * math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        """Calculate the surface area of the cone."""
        slant_height = (self.radius**2 + self.height**2) ** 0.5
        return math.pi * self.radius * (self.radius + slant_height)

    def radius_from_volume(self, volume):
        """Calculate radius from volume and height."""
        return ((3 * volume) / (math.pi * self.height)) ** (1/2)

    def height_from_volume(self, volume):
        """Calculate height from volume and radius."""
        return (3 * volume) / (math.pi * self.radius ** 2)


class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        """Calculate the volume of the cube."""
        return self.side_length ** 3

    def surface_area(self):
        """Calculate the surface area of the cube."""
        return 6 * self.side_length ** 2

    def side_from_volume(self, volume):
        """Calculate side length from volume."""
        return volume ** (1/3)

    def side_from_surface_area(self, surface_area):
        """Calculate side length from surface area."""
        return (surface_area / 6) ** 0.5


class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """Calculate the volume of the cuboid."""
        return self.length * self.width * self.height

    def surface_area(self):
        """Calculate the surface area of the cuboid."""
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

    def length_from_volume(self, volume, width, height):
        """Calculate length from volume, width, and height."""
        return volume / (width * height)

    def width_from_volume(self, volume, length, height):
        """Calculate width from volume, length, and height."""
        return volume / (length * height)

    def height_from_volume(self, volume, length, width):
        """Calculate height from volume, length, and width."""
        return volume / (length * width)


class Pyramid:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        return (1 / 3) * self.base_area * self.height

    def surface_area(self, base_perimeter, slant_height):
        lateral_area = (1 / 2) * base_perimeter * slant_height
        return self.base_area + lateral_area

    def height_from_volume(self, volume):
        """Calculate height from volume and base area."""
        return (3 * volume) / self.base_area

    def base_area_from_volume(self, volume):
        """Calculate base area from volume and height."""
        return (3 * volume) / self.height


class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """Calculate the volume of the rectangular prism."""
        return self.length * self.width * self.height

    def surface_area(self):
        """Calculate the surface area of the rectangular prism."""
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

    def length_from_volume(self, volume, width, height):
        """Calculate length from volume, width, and height."""
        return volume / (width * height)

    def width_from_volume(self, volume, length, height):
        """Calculate width from volume, length, and height."""
        return volume / (length * height)

    def height_from_volume(self, volume, length, width):
        """Calculate height from volume, length, and width."""
        return volume / (length * width)


class Torus:
    def __init__(self, major_radius, minor_radius):
        self.major_radius = major_radius  # Distance from the center of the tube to the center of the torus
        self.minor_radius = minor_radius    # Radius of the tube

    def volume(self):
        """Calculate the volume of the torus."""
        return (2 * math.pi ** 2) * self.major_radius * self.minor_radius ** 2

    def surface_area(self):
        """Calculate the surface area of the torus."""
        return (2 * math.pi ** 2) * self.major_radius * self.minor_radius

    def major_radius_from_volume(self, volume, minor_radius):
        """Calculate major radius from volume and minor radius."""
        return volume / (2 * math.pi ** 2 * minor_radius ** 2)

    def minor_radius_from_volume(self, volume, major_radius):
        """Calculate minor radius from volume and major radius."""
        return ((volume / (2 * math.pi ** 2 * major_radius)) ** (1/2))


class Ellipsoid:
    def __init__(self, semi_major_axis, semi_minor_axis, semi_intermediate_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.semi_intermediate_axis = semi_intermediate_axis

    def volume(self):
        """Calculate the volume of the ellipsoid."""
        return (4/3) * math.pi * self.semi_major_axis * self.semi_minor_axis * self.semi_intermediate_axis

    def surface_area(self):
        """Approximate the surface area of the ellipsoid."""
        p = 1.6075  # Approximation constant
        return 4 * math.pi * ((self.semi_major_axis**p * self.semi_minor_axis**p +
                                self.semi_major_axis**p * self.semi_intermediate_axis**p +
                                self.semi_minor_axis**p * self.semi_intermediate_axis**p) / 3) ** (1/p)

    @staticmethod
    def semi_major_from_volume(volume, semi_minor_axis, semi_intermediate_axis):
        """Calculate semi-major axis from volume and other axes."""
        return (3 * volume) / (4 * math.pi * semi_minor_axis * semi_intermediate_axis)

    @staticmethod
    def semi_minor_from_volume(volume, semi_major_axis, semi_intermediate_axis):
        """Calculate semi-minor axis from volume and other axes."""
        return (3 * volume) / (4 * math.pi * semi_major_axis * semi_intermediate_axis)

    @staticmethod
    def semi_intermediate_from_volume(volume, semi_major_axis, semi_minor_axis):
        """Calculate semi-intermediate axis from volume and other axes."""
        return (3 * volume) / (4 * math.pi * semi_major_axis * semi_minor_axis)


class Octahedron:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def volume(self):
        """Calculate the volume of the octahedron."""
        return (1/3) * math.sqrt(2) * self.edge_length ** 3

    def surface_area(self):
        """Calculate the surface area of the octahedron."""
        return 2 * math.sqrt(3) * self.edge_length ** 2

    @staticmethod
    def edge_length_from_volume(volume):
        """Calculate edge length from volume."""
        return ((3 * volume) / (math.sqrt(2))) ** (1/3)

    @staticmethod
    def edge_length_from_surface_area(surface_area):
        """Calculate edge length from surface area."""
        return math.sqrt(surface_area / (2 * math.sqrt(3)))


class Dodecahedron:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def volume(self):
        """Calculate the volume of the dodecahedron."""
        return (15 + 7 * math.sqrt(5)) / 4 * self.edge_length ** 3

    def surface_area(self):
        """Calculate the surface area of the dodecahedron."""
        return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * self.edge_length ** 2

    @staticmethod
    def edge_length_from_volume(volume):
        """Calculate edge length from volume."""
        return ((volume * 4) / (15 + 7 * math.sqrt(5))) ** (1/3)

    @staticmethod
    def edge_length_from_surface_area(surface_area):
        """Calculate edge length from surface area."""
        return (surface_area / (3 * math.sqrt(25 + 10 * math.sqrt(5)))) ** (1/2)


class Frustum:
    def __init__(self, radius_top, radius_bottom, height):
        self.radius_top = radius_top
        self.radius_bottom = radius_bottom
        self.height = height

    def volume(self):
        """Calculate the volume of the frustum."""
        return (1/3) * math.pi * self.height * (self.radius_top ** 2 + self.radius_bottom ** 2 + self.radius_top * self.radius_bottom)

    def surface_area(self):
        """Calculate the surface area of the frustum."""
        slant_height = ((self.radius_bottom - self.radius_top) ** 2 + self.height ** 2) ** 0.5
        lateral_area = math.pi * (self.radius_top + self.radius_bottom) * slant_height
        top_area = math.pi * self.radius_top ** 2
        bottom_area = math.pi * self.radius_bottom ** 2
        return lateral_area + top_area + bottom_area

    @staticmethod
    def height_from_volume(volume, radius_top, radius_bottom):
        """Calculate height from volume and both radii."""
        return (3 * volume) / (math.pi * (radius_top ** 2 + radius_bottom ** 2 + radius_top * radius_bottom))

    @staticmethod
    def radius_top_from_volume(volume, radius_bottom, height):
        """Calculate top radius from volume and bottom radius."""
        return ((3 * volume) / (math.pi * height) - radius_bottom ** 2) / radius_bottom


class PentagonalPrism:
    def __init__(self, side_length, height):
        self.side_length = side_length
        self.height = height

    def volume(self):
        """Calculate the volume of the pentagonal prism."""
        base_area = (5 * self.side_length ** 2) / (4 * math.tan(math.pi / 5))
        return base_area * self.height

    def surface_area(self):
        """Calculate the surface area of the pentagonal prism."""
        base_area = (5 * self.side_length ** 2) / (4 * math.tan(math.pi / 5))
        lateral_area = 5 * self.side_length * self.height
        return (2 * base_area) + lateral_area

    @staticmethod
    def side_length_from_volume(volume, height):
        """Calculate side length from volume and height."""
        base_area = volume / height
        return ((4 * base_area * math.tan(math.pi / 5)) / 5) ** (1/2)

    @staticmethod
    def height_from_volume(volume, side_length):
        """Calculate height from volume and side length."""
        base_area = (5 * side_length ** 2) / (4 * math.tan(math.pi / 5))
        return volume / base_area


import math

class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        """Calculate the volume of the prism."""
        return self.base_area * self.height

    def surface_area(self, base_perimeter):
        """Calculate the surface area of the prism."""
        lateral_area = base_perimeter * self.height
        return 2 * self.base_area + lateral_area

    @staticmethod
    def base_area_from_volume(volume, height):
        """Calculate the base area from the volume and height."""
        return volume / height

    @staticmethod
    def height_from_volume(volume, base_area):
        """Calculate the height from the volume and base area."""
        return volume / base_area
