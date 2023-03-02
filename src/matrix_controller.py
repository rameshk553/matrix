from matrix.matrix import Matrix
from matrix.matrix_view import MatrixView


class MatrixController:
    def __init__(self):
        self._view = MatrixView(self)
        self._model = Matrix()

    def start(self):
        self._view.start()

    def add(self, matrix1, matrix2):
        result = self._model.add(matrix1, matrix2)
        self._view.display(result)

