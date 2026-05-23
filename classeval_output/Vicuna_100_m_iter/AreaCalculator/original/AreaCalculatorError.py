import math
class AreaCalculator:  
    """
    This is a class for calculating the area of different shapes, including circle, sphere, cylinder, sector and annulus.
    """

    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius



    def calculate_circle_area(self):
            """
            calculate the area of circle based on self.radius
            :return: area of circle, float
            >>> areaCalculator = AreaCalculator(2)
            >>> areaCalculator.calculate_circle_area()
            12.566370614359172
            """
            return 3.14159 * self.radius**2

    def calculate_sphere_area(self):
            """
            calculate the area of sphere based on self.radius
            :return: area of sphere, float
            >>> areaCalculator = AreaCalculator(2)
            >>> areaCalculator.calculate_sphere_area()
            50.26548245743669
            """
            return 4 * 3.14159 * self.radius**3

    def calculate_cylinder_area(self, height):
            """
            calculate the area of cylinder based on self.radius and height
            :param height: height of cylinder, float
            :return: area of cylinder, float
            >>> areaCalculator = AreaCalculator(2)
            >>> areaCalculator.calculate_cylinder_area(3)
            62.83185307179586
            """
            radius = self.radius
            height = height * 2
            area = 2 * 3.14159 * radius * height
            return area

    def calculate_sector_area(self, angle):
            """
            calculate the area of sector based on self.radius and angle
            :param angle: angle of sector, float
            :return: area of sector, float
            >>> areaCalculator = AreaCalculator(2)
            >>> areaCalculator.calculate_sector_area(math.pi)
            6.283185307179586
            """
            radius = self.radius
            height = radius * math.cos(angle)
            area = 2 * math.pi * radius * height
            return area