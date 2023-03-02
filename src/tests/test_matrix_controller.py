import unittest
from unittest import mock
from hamcrest import assert_that, equal_to
from src.matrix_controller import MatrixController


class TestMatrixController(unittest.TestCase):
    def setUp(self):
        self.mock_view = mock.MagicMock()
        self.controller = MatrixController()
        self.controller._view = self.mock_view

    def test_add_calls_matrix_view_display_only_once_with_addition_result(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = [[6, 8], [10, 12]]

        self.controller.add(matrix1, matrix2)

        self.mock_view.display.assert_called_once_with(expected_result)

    def test_add_calls_matrix_view_display_when_matrix_dimension_is_different(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6, 7], [7, 8]]

        self.controller.add(matrix1, matrix2)

        assert_that(str(self.mock_view.display.call_args[0][0]), equal_to("Matrices are not of the same dimensions"))

    def test_start_starts_the_matrix_view(self):
        self.controller.start()

        self.mock_view.start.assert_called_once()
