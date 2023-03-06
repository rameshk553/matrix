import ast
import re
from src.matrix_operation import MatrixOperation


class MatrixView:
    def __init__(self, controller):
        self._controller = controller
        self._selected_operation = None
        self._matrix1 = None
        self._matrix2 = None
        self.operations = {
            MatrixOperation.ADDITION: self._create_addition_matrix,
            MatrixOperation.MULTIPLICATION: self._create_multiplication_matrix,
            MatrixOperation.INVERSE: self._create_inverse_matrix
        }

    def start(self):
        self._selected_operation = MatrixView.select_operation()
        self.create_matrix(self._selected_operation)
        if self._matrix1 is not None:
            self.perform_operation(self._matrix1, self._matrix2, self._selected_operation)

    @staticmethod
    def select_operation():
        while True:
            user_input = input(
                "Enter the number corresponding to a matrix operation:\n "
                "1 - Addition, "
                "2 - Multiplication, "
                "3 - Inverse:\n "
            )
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input in [1, 2, 3]:
                    return MatrixOperation(user_input)
                    break
                else:
                    print("Enter a value between 1 and 3")
            else:
                print("Invalid input, enter a valid integer")

    def create_matrix(self, matrix_operation):
        self.operations[matrix_operation]()

    def perform_operation(self, matrix1, matrix2, selected_operation):
        if selected_operation == MatrixOperation.ADDITION:
            self._controller.add(matrix1, matrix2)

    def _create_addition_matrix(self):
        self._matrix1 = self._get_matrix_data(1)
        self._matrix2 = self._get_matrix_data(2)

    def _create_multiplication_matrix(self):
        pass

    def _create_inverse_matrix(self):
        pass

    @staticmethod
    def _get_matrix_data(number):
        pattern = r"^[a-zA-Z0-9,\[\]]+$"
        data = None
        while True:
            user_input = input(
                f"Enter matrix {number} data:\n"
                "Example: For creating a 2x3 matrix, please type: \n"
                "[[1,2,3],[4,5,6]]\n"
            )
            if re.match(pattern, user_input):
                try:
                    result = ast.literal_eval(user_input)
                    if isinstance(result, list):
                        data = result
                        break
                except Exception as e:
                    print(e)
            else:
                print("input is invalid")

        return data

    @staticmethod
    def display(matrix):
        print(matrix)
