class Cell:
    def __init__(self, c):
        self.c = int(c)

    def __str__(self):
        return f'Ответ: {self.c * "*"}'

    def __add__(self, qwe):
           return Cell(self.c + qwe.c)

    def __sub__(self, qwe):

        return self.c - qwe.c if (self.c - qwe.c) > 0 else print('Меньше 0')

    def __mul__(self, qwe):
        return Cell(int(self.c * qwe.c))

    def __truediv__(self, qwe):
        return Cell(round(self.c // qwe.c))


    def make_order(self, cellsss):
        row = ''
        for i in range(int(self.c / cellsss)):
            row += f'{"*" * cellsss} \\n'
        row += f'{"*" * (self.c % cellsss)}'
        return row

cell1 = Cell(40)
cell2 = Cell(26)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 / cell2)