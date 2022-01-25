class Matrix:
    def __init__(self, matrix_string):
        self.raw = matrix_string
        self.rows = [[int(n) for n in row.split()] for row in self.raw.splitlines()]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        column = []
        for row in self.rows:
            column.append(row[index - 1])
        return column
