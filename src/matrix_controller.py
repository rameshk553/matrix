from src.matrix import Matrix
from src.matrix_view import MatrixView


class MatrixController:
    def __init__(self):
        self._view = MatrixView(self)

    def start(self):
        self._view.start()

    def add(self, matrix1, matrix2):
        matrix1 = Matrix(matrix1)
        matrix2 = Matrix(matrix2)
        result = matrix1 + matrix2
        self._view.display(result.values)
