class Matrix:
    def __init__(self, l_1, l_2):
        # self.m = [l_1, l_2]
        self.l_1 = l_1
        self.l_2 = l_2

    def __add__(self):
        m = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.l_1)):

            for j in range(len(self.l_2[i])):
                m[i][j] = self.l_1[i][j] + self.l_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))



m1 = Matrix([[3, 29, 12],
                    [8, 19, 20],
                    [5, 30, 7]],
                   [[34, 20, 4],
                    [67, 12, 15],
                    [12, 15, 19]])

print(m1.__add__())