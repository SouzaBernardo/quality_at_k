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



    def calculate_circle_area(self, radius: float = 2.0):
        """
        calculate the area of circle based on self.radius
        :return: area of circle, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_circle_area()
        12.566370614359172
        """
        return math.pi * radius ** 2



    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        """
        return math.pi * (self.radius ** 2) * height

    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        """
        area = 0.0
        for i in range(1, 3):
            r = self.radius // 2
            theta = angle // 2 * math.pi
            area += r * math.sin(theta) * (i - 1) ** 2
        return area / 3.0