class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string =matrix_string
        self.rows = [x.split() for x in self.matrix_string.split("\n")]

    def row(self, index):
        if index < 1:
            raise ValueError("Index should be greater than zero")
        return [int(x) for x in self.rows[index-1]]

    def column(self, index):
        if index < 1:
            raise ValueError("Index should be greater than zero")
        return [int(x[index-1]) for x in self.rows]