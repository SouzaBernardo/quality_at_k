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

    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """

    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """

    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """

    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and out_radius
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of annulus, float
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """

    def calculate_area(self):
        """
        calculate the area of the shape
        :return: area of the shape, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area()
        12.566370614359172
        """

    def calculate_area_of_circle(self):
        """
        calculate the area of the circle
        :return: area of the circle, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_circle()
        12.566370614359172
        """

    def calculate_area_of_sphere(self):
        """
        calculate the area of the sphere
        :return: area of the sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_sphere()
        50.26548245743669
        """

    def calculate_area_of_cylinder(self, height):
        """
        calculate the area of the cylinder
        :param height: height of cylinder, float
        :return: area of the cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_cylinder(3)
        62.83185307179586
        """

    def calculate_area_of_sector(self, angle):
        """
        calculate the area of the sector
        :param angle: angle of sector, float
        :return: area of the sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_sector(math.pi)
        6.283185307179586
        """

    def calculate_area_of_annulus(self, inner_radius, outer_radius):
        """
        calculate the area of the annulus
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of the annulus, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_annulus(2, 3)
        15.707963267948966
        """

    def calculate_area_of_circle_and_annulus(self):
        """
        calculate the area of the circle and annulus
        :return: area of the circle and annulus, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_circle_and_annulus()
        12.566370614359172
        """

    def calculate_area_of_circle_and_sphere(self):
        """
        calculate the area of the circle and sphere
        :return: area of the circle and sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_circle_and_sphere()
        12.566370614359172
        """

    def calculate_area_of_circle_and_cylinder(self, height):
        """
        calculate the area of the circle and cylinder
        :param height: height of cylinder, float
        :return: area of the circle and cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_circle_and_cylinder(3)
        50.26548245743669
        """

    def calculate_area_of_circle_and_sector(self, angle):