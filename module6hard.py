# Наследование классов
from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides, filled=bool):
        self.__sides = [*sides] if len(sides) == self.sides_count else [
            sides[0] if isinstance(self, Cube) and len(sides) == 1 else 1 for _ in range(self.sides_count)]
        self.__color = [*color]
        self.filled = filled

    def __len__(self):
        return sum(self.__sides)

    @staticmethod
    def __is_valid_color(color):
        return len(color) == 3 and 0 <= color[0] <= 255 and 0 <= color[1] and 0 <= color[2]

    def __is_valid_sides(self, sides):
        return len(sides) == self.sides_count

    def get_color(self):
        return self.__color

    def set_color(self, *color):
        if self.__is_valid_color(color): self.__color = [*color]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides): self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *radius):
        super().__init__(color, *radius)
        self.__radius = round(self.get_sides()[0] / (2 * pi), 2)

    def get_square(self):
        return round(pi * self.__radius ** 2, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *side):
        super().__init__(color, *side)

    def get_volume(self):
        return self.get_sides()[0] ** 3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        return round(1 / 4 * ((2 * a * b) ** 2 - (a ** 2 + b ** 2 - c ** 2) ** 2) ** 0.5, 2)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 3, 4, 5)
triangle2 = Triangle((33, 44, 66), 12, 56)

circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())

triangle1.set_sides(412, 45)
print(triangle1.get_sides())
print(triangle2.get_sides())
