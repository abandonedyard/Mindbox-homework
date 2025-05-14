import unittest
import math
from shapes import Circle, Triangle, compute_area


class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area(), math.pi * 4)
        self.assertAlmostEqual(compute_area(c), math.pi * 4)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-5)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)
        self.assertAlmostEqual(compute_area(t), 6.0)

    def test_is_right(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertFalse(Triangle(5, 5, 5).is_right())

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)     # несуществующий
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)    # отрицательная сторона


if __name__ == "__main__":
    unittest.main()
