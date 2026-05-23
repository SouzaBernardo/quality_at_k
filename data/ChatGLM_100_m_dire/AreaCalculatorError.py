import math
class AreaCalculator: 
    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius



    def calculate_circle_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_sphere_area(self):
        area = math.pi * (self.radius ** 2)
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
        area = 2 * math.pi * self.radius * (1 - (1 / math.cos(angle)))
        return area