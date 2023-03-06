class Matrix:

    def __init__(self, values):
        self.values = values
    def __add__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise ValueError("Can only add matrices together")
            if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
                return ValueError("Matrices are not of the same dimensions")
            result = []
            for i in range(len(self.values)):
                row = []
                for j in range(len(self.values[0])):
                    row.append(self.values[i][j] + other.values[i][j])
                result.append(row)

            return Matrix(result)
        except TypeError as e:
            return str(e)
