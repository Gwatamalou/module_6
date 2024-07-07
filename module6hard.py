import math


class Figure:
    side_count = 0

    def __init__(self, color, args):
        self.__sides = None
        self.__color = None
        self.filled = False
        self.set_side(*args)
        self.set_color(*color)

    def __len__(self):
        return sum(x for x in self.__sides)

    def __is_valid_color(self, r, g, b):
        return True if r >= 0 and g >= 0 and b >= 0 and r < 255 and g < 255 and b < 255 else False

    def __is_valid_sides(self, args):
        return True if len(args) == self.side_count and all(isinstance(x, int) for x in args) else False

    def get_color(self):
        return self.__color

    def get_side(self):
        return self.__sides

    def set_color(self, r, g, b):
        if not self.__color:
            self.__color = [r, g, b] if self.__is_valid_color(r, g, b) else 'Цвет должен быть в формате RGB'
        elif self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_side(self, *args):
        if not self.__sides:
            self.__sides = list(args) if self.__is_valid_sides(args) else list([1] * self.side_count)
        elif self.__is_valid_sides(args):
            self.__sides = list(args)


class Circle(Figure):
    side_count = 1

    def __init__(self, color, *args):
        super().__init__(color, args)
        self.__radius = int(self.get_side()[0]) / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    side_count = 3

    def __init__(self, color, *args):
        super().__init__(color, *args)
        self.__height = self.__triangle_height()

    def __triangle_height(self):
        rib = self.get_side()
        p = (sum(rib)) / 2
        try:
            h = (2 * math.sqrt(p * (p - rib[0]) * (p - rib[1]) * (p - rib[2]))) / rib[0]
        except:
            return 'Такого треугольника не существует'
        return h

    def get_square(self):
        return 'Треугольник не существует' if isinstance(self.__height, str) else max(
            self.get_side()) * self.__height / 2


class Cube(Figure):
    side_count = 12

    def __init__(self, color, *args):
        self.__sides = None
        super().__init__(color, args)

    def __is_valid_sides(self, args):
        return True if (len(args) == 1 or len(args) == self.side_count) and isinstance(args[0], int) and all(x == args[0] for x in args) else False

    def set_side(self, *args):
        if self.__sides is None:
            self.__sides = list([args[0]]*self.side_count) if self.__is_valid_sides(args) else list([1] * self.side_count)
        elif self.__is_valid_sides(args):
            self.__sides = list([args[0]] * self.side_count)


    def get_side(self):
        return self.__sides


    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_side(5, 3, 12, 4, 5) # Не изменится
circle1.set_side(15) # Изменится
print(cube1.get_side())
print(circle1.get_side())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
