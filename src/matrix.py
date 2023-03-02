
class Matrix:
    def add(self, matrix1, matrix2):
        try:
            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                return ValueError("Matrices are not of the same dimensions")
            result = []
            for i in range(len(matrix1)):
                row = []
                for j in range(len(matrix1[0])):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result.append(row)
            return result
        except TypeError as e:
            return str(e)


