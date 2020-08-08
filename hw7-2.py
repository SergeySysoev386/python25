class Material:
    def __init__(self, size, height):
        self.v = size
        self.h = height

    def get_coatarea(self):
        return self.v / 6.5 + 0.5

    def get_suitarea(self):
        return self.h * 2 + 0.3

    @property
    def get_fullarea(self):
        return str(f'Всего материала:'
                   f' {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')


class Coat(Material):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.coatarea = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'материал для пальто: {self.coatarea}'


class Suit(Material):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suitarea = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'материал для костюма: {self.suitarea}'


coat = Coat(2, 5)
suit = Suit(3, 4)
print(coat)
print(coat.get_fullarea)
print(suit)
print(suit.get_fullarea)
