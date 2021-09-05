list_1 = [[1, 10, 8], [16, 7, 25], [5, 13, 11]]
list_2 = [[17, 0, 2], [4, 9, 2], [41, 18, 81]]


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join(map(str, self.list_of_lists))

    def __add__(self, other):
        list_sum = []
        for i in range(len(self.list_of_lists)):
            list_sum.append([])
            for j in range(len(self.list_of_lists[0])):
                list_sum[i].append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
        return '\n'.join(map(str, list_sum))


matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)

print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
