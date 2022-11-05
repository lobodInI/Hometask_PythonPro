import unittest
from coord_point import Coordinates


class TestLenLine(unittest.TestCase):
    point1_start = Coordinates(15, 15)
    point2_start = Coordinates(23, 21)
    point2_1 = Coordinates(21, 7)
    point2_2 = Coordinates(7, 9)
    point2_3 = Coordinates(9, 23)
    point2_4 = Coordinates(15, 25)
    point2_5 = Coordinates(25, 15)
    point2_6 = Coordinates(-1, 3)
    point2_7 = Coordinates(-1, 27)
    point2_8 = Coordinates(-5, -6)
    point2_9 = Coordinates(3, -1)
    point2_10 = Coordinates(27, -1)
    point1_1 = Coordinates(29, 29)
    point1_2 = Coordinates(29, 13)
    point1_3 = Coordinates(17, 29)
    point1_4 = Coordinates(-1, 3)
    point1_5 = Coordinates(-1, 39)
    point1_6 = Coordinates(-17, -21)
    point1_7 = Coordinates(2, -7)
    point1_8 = Coordinates(44, -7)
    point1_zero = Coordinates(0, 0)
    point2_zero = Coordinates(0, 0)

    def test_1(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_start))

    def test_2(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_1))

    def test_3(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_2))

    def test_4(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_3))

    def test_5(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_4))

    def test_6(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point1_start, self.point2_5))

    def test_7(self):
        self.assertEqual(20.0, Coordinates.line_length(self.point1_start, self.point2_6))

    def test_8(self):
        self.assertEqual(20.0, Coordinates.line_length(self.point1_start, self.point2_7))

    def test_9(self):
        self.assertEqual(29.0, Coordinates.line_length(self.point1_start, self.point2_8))

    def test_10(self):
        self.assertEqual(20.0, Coordinates.line_length(self.point1_start, self.point2_9))

    def test_11(self):
        self.assertEqual(20.0, Coordinates.line_length(self.point1_start, self.point2_10))

    def test_12(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point2_start, self.point1_1))

    def test_13(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point2_start, self.point1_2))

    def test_14(self):
        self.assertEqual(10.0, Coordinates.line_length(self.point2_start, self.point1_3))

    def test_15(self):
        self.assertEqual(30.0, Coordinates.line_length(self.point2_start, self.point1_4))

    def test_16(self):
        self.assertEqual(30.0, Coordinates.line_length(self.point2_start, self.point1_5))

    def test_17(self):
        self.assertEqual(58.0, Coordinates.line_length(self.point2_start, self.point1_6))

    def test_18(self):
        self.assertEqual(35.0, Coordinates.line_length(self.point2_start, self.point1_7))

    def test_19(self):
        self.assertEqual(35.0, Coordinates.line_length(self.point2_start, self.point1_8))

    def test_20(self):
        self.assertEqual(0.0, Coordinates.line_length(self.point1_zero, self.point2_zero))
