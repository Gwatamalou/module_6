


class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'yellow', 'black']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):

        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):

        return f'Модель: {self.__model}'

    def get_horsepower(self):

        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):

        return f'Цвет: {self.__color}'

    def print_info(self):

        print(f'{self.get_model()}\n'
              f'{self.get_horsepower()}\n'
              f'{self.get_color()}\n'
              f'Владелец: {self.owner}')

    def set_color(self, color: str):
        if color.lower() in  self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Невозможно покрасить в {color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
