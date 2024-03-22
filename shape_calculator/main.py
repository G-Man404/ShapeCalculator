import math


class ShapeCalculator:
    @staticmethod
    def get_circle_area(radius: float):
        """Calculating the shape_calculator of a square"""
        return math.pi * radius ** 2

    @staticmethod
    def get_triangle_area(side1: float, side2: float, side3: float):
        """Calculating the shape_calculator of a triangle"""
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1: float, side2: float, side3: float):
        """Checking whether the triangle is rectangular"""
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    @staticmethod
    def get_area(*args):
        """Calculates the shape_calculator of a shape without knowing the type of shape in compile-time."""
        if len(args) == 1:
            return ShapeCalculator.get_circle_area(args[0])
        elif len(args) == 3:
            return ShapeCalculator.get_triangle_area(*args)
        else:
            raise ValueError("unidentified form")
