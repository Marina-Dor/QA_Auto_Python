from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Diamond(Shape):
    def __init__(self, side_a, diagonal_1, diagonal_2):
        self.__side_a = side_a
        self.__diagonal_1 = diagonal_1
        self.__diagonal_2 = diagonal_2

    def perimeter(self):
        return 4 * self.__side_a

    def area(self):
        return (self.__diagonal_1 * self.__diagonal_2) / 2


class Square(Shape):
    def __init__(self, side_a):
        self.__side_a = side_a

    def perimeter(self):
        return 4 * self.__side_a

    def area(self):
        return self.__side_a * self.__side_a


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def area(self):
        return self.__side_a * self.__side_b


shapes = [Diamond(5, 10, 15),
          Square(6),
          Rectangle(10, 12)]

for shape in shapes:
    shape_name = shape.__class__.__name__
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"{shape_name} - Area: {area}, Perimeter: {perimeter}")
