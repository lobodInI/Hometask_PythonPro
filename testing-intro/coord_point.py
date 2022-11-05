from math import sqrt


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     return Coordinates(self.x + other.x, self.y + other.y)
    #
    # def __repr__(self):
    #     return f"x: {self.x}, y: {self.y}"

    @staticmethod
    def line_length(point1, point2):
        return sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))


if __name__ == '__main__':
    point_1 = Coordinates(15, 15)
    point_2 = Coordinates(-1, 3)

    print("len of line: ", Coordinates.line_length(point_1, point_2))
    # print(point_1+point_2)
