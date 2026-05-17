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
        calculate the area of all shapes
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area()
        12.566370614359172
        """

    def calculate_area_of_all_shapes(self):
        """
        calculate the area of all shapes
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_all_shapes()
        12.566370614359172
        """

    def calculate_area_of_all_shapes_with_radius(self, radius):
        """
        calculate the area of all shapes
        :param radius: radius of shape, float
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_all_shapes_with_radius(2)
        12.566370614359172
        """

    def calculate_area_of_all_shapes_with_radius_and_height(self, radius, height):
        """
        calculate the area of all shapes
        :param radius: radius of shape, float
        :param height: height of shape, float
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_all_shapes_with_radius_and_height(2, 3)
        12.566370614359172
        """

    def calculate_area_of_all_shapes_with_radius_and_height_and_angle(self, radius, height, angle):
        """
        calculate the area of all shapes
        :param radius: radius of shape, float
        :param height: height of shape, float
        :param angle: angle of shape, float
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_all_shapes_with_radius_and_height_and_angle(2, 3, math.pi)
        12.566370614359172
        """

    def calculate_area_of_all_shapes_with_radius_and_height_and_angle_and_radius(self, radius, height, angle, inner_radius, outer_radius):
        """
        calculate the area of all shapes
        :param radius: radius of shape, float
        :param height: height of shape, float
        :param angle: angle of shape, float
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of all shapes, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_area_of_all_shapes_with_radius_and_height_and_angle_and_radius(2, 3, math.pi, 2, 3)
        12.566370614359172
        """

    def calculate_area_of_all_shapes_with_radius_and_height_and_angle_and_radius_and_height(self, radius, height, angle, inner_radius, outer_radius, inner_height, outer_height):
        """
        calculate the area of all shapes
        :param radius: radius of shape, float
        :param height: height of shape, float
        :param angle: angle of shape, float
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :param inner_height: inner height of sector, float
        :