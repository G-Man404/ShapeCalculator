import math
import unittest
from shape_calculator import ShapeCalculator


class TestGeometry(unittest.TestCase):
    def test_get_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.get_circle_area(1), math.pi)
        self.assertAlmostEqual(ShapeCalculator.get_circle_area(0), 0)
        self.assertAlmostEqual(ShapeCalculator.get_circle_area(5), 25 * math.pi)

    def test_get_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.get_triangle_area(3, 4, 5), 6)
        self.assertAlmostEqual(ShapeCalculator.get_triangle_area(6, 8, 10), 24)
        self.assertAlmostEqual(ShapeCalculator.get_triangle_area(5, 5, 5), 10.825317547305485)

    def test_get_area(self):
        self.assertAlmostEqual(ShapeCalculator.get_area(3, 4, 5), 6)
        self.assertAlmostEqual(ShapeCalculator.get_area(6, 8, 10), 24)
        self.assertAlmostEqual(ShapeCalculator.get_area(1), math.pi)
        self.assertAlmostEqual(ShapeCalculator.get_area(0), 0)

    def test_get_unknown_shape(self):
        with self.assertRaises(ValueError):
            ShapeCalculator.get_area(1, 2)
            ShapeCalculator.get_area(1, 2, 3, 4)


if __name__ == '__main__':
    unittest.main()
