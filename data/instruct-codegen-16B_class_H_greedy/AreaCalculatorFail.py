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
        """
        return self.radius * self.radius * math.pi
    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        """
        return 4 * self.radius * self.radius * math.pi
    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        """
        return self.radius * self.radius * height
    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        """
        return self.radius * self.radius * angle / 2
    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and outer_radius
        :param inner_radius: inner radius of annulus, float
        :param outer_radius: outer radius of annulus, float
        :return: area of annulus, float
        """
        return self.radius * self.radius * (outer_radius - inner_radius)