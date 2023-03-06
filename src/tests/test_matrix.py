import unittest

from hamcrest import assert_that, equal_to, instance_of
from src.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_add_returns_addition_two_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        expected_result = [[6, 8], [10, 12]]

        result = matrix1 + matrix2

        assert_that(result.values, equal_to(expected_result))

    def test_add_returns_value_error_when_two_matrices_dimensions_are_not_same(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6, 7], [7, 8]])

        result = matrix1 + matrix2

        assert_that(result, instance_of(ValueError))

    def test_add_returns_type_error_when_matrices_are_of_different_type(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([["a", "b"], [7, 8]])
        expected_result = "unsupported operand type(s) for +: 'int' and 'str'"

        result = matrix1 + matrix2

        assert_that(result, equal_to(expected_result))
