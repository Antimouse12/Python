class Cell:
    def __init__(self, qty_of_cells: int):
        self.qty_of_cells = qty_of_cells

    def __add__(self, other):
        return Cell(self.qty_of_cells + other.qty_of_cells)

    def __sub__(self, other):
        if (self.qty_of_cells - other.qty_of_cells) > 0:
            return Cell(self.qty_of_cells - other.qty_of_cells)
        else:
            print(f'impossible operation')

    def __mul__(self, other):
        return Cell(self.qty_of_cells * other.qty_of_cells)

    def __truediv__(self, other):
        return Cell(round(self.qty_of_cells / other.qty_of_cells))

    def make_order(self, rows: int, qty_of_cells):
        return '\n'.join(['*' * rows for _ in range(qty_of_cells // rows)]) + '\n' + '*' * (qty_of_cells % rows)

    def __str__(self):
        return f'клетка состоит из {self.qty_of_cells} ячеек'


cell_1 = Cell(25)
cell_2 = Cell(15)

print(cell_1)
print(cell_2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print((cell_1 * cell_2).make_order(4, 10))
