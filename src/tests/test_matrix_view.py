import mock
import unittest
from hamcrest import assert_that, equal_to
from src.matrix_operation import MatrixOperation
from src.matrix_view import MatrixView

class TestMatrixView(unittest.TestCase):
    def setUp(self):
        self.controller = mock.MagicMock()
        self.view = MatrixView(self.controller)

    def test_select_operation_returns_matrix_operation_addition_when_input_value_is_1(
        self,
    ):
        with mock.patch("builtins.input", return_value="1"):
            result = self.view.select_operation()

        self.assertEqual(result, MatrixOperation.ADDITION)

    def test_select_operation_prints_a_message_when_input_is_invalid(self):
        with mock.patch("builtins.input", side_effect=[4, 1]):
            with mock.patch("builtins.print") as mock_print:
                _ = self.view.select_operation()

        mock_print.assert_called_once_with("Enter a value between 1 and 3")

    def test_select_operation_prints_value_error_message_when_input_is_a_letter(self):
        with mock.patch("builtins.input", side_effect=["a", 1]):
            with mock.patch("builtins.print") as mock_print:
                _ = self.view.select_operation()

        mock_print.assert_called_once_with("Value error")

    def test_create_matrix_calls_for_user_input_twice_when_matrix_addition_operation_selected(
        self,
    ):
        with mock.patch(
            "builtins.input",
            side_effect=[
                "[[1,2],[3,4]]",
                "[[5,6],[7,8]]",
                "[[5,6],[7,8]]",
                "[[5,6],[7,8]]",
            ],
        ) as mock_input:
            self.view.create_matrix(MatrixOperation.ADDITION)

        assert_that(mock_input.call_count, equal_to(2))

    def test_create_matrix_prints_a_message_when_user_input_has_exception(self):
        with mock.patch(
            "builtins.input",
            side_effect=[
                [[1, 2], [3, 4]],
                "[[5,6],[7,8]]",
                "[[5,6],[7,8]]",
                "[[5,6],[7,8]]",
            ],
        ):
            with mock.patch("builtins.print") as mock_print:
                self.view.create_matrix(MatrixOperation.ADDITION)

        mock_print.assert_called_once()

    def test_perform_operation_calls_controller_add_method_with_passed_in_arguments(
        self,
    ):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        selected_operation = MatrixOperation.ADDITION
        mock_add = mock.Mock()
        self.controller.add = mock_add

        self.view.perform_operation(matrix1, matrix2, selected_operation)

        mock_add.assert_called_once_with(matrix1, matrix2)

    def test_display_calls_print_with_passed_in_data(self):
        with mock.patch("builtins.print") as mock_print:
            matrix = [[1, 2], [3, 4]]

            MatrixView.display(matrix)

            mock_print.assert_called_with(matrix)
