import unittest
from lesson_09.src.homework_09 import splitting_string_list_to_numbers_and_adding
from lesson_09.src.homework_09 import the_arithmetic_mean_of_the_list
from unittest.mock import patch
from io import StringIO


class SplittingStringListToNumbersAndAddingTest(unittest.TestCase):
    # Positive tests
    def test_split_single_list(self):
        result = splitting_string_list_to_numbers_and_adding(["1, 2, 5, 4, 10, -6"])

        expected_result = [[1, 2, 5, 4, 10, -6]]

        self.assertEqual(result, expected_result)

    def test_split_two_lists(self):
        result = splitting_string_list_to_numbers_and_adding(["1, 2, 5, 4, 10, -6", "1, 8, 9"])

        expected_result = [[1, 2, 5, 4, 10, -6], [1, 8, 9]]

        self.assertEqual(result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_sum_of_single_list_with_positive_negative_numbers(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding(["1, -2, 5, 4, 0, 10"])

        output = mock_stdout.getvalue().strip()

        expected_result = 18

        self.assertEqual(int(output), expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_sum_of_single_number(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding(["10"])

        output = mock_stdout.getvalue().strip()

        expected_result = 10

        self.assertEqual(int(output), expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_sum_of_two_lists(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding(["1, -2, 5, 4, 0, 10", "1, 9, 5, 7, 8"])

        output = mock_stdout.getvalue().strip()
        results = output.split('\n')

        result1 = int(results[0])
        result2 = int(results[1])

        expected_result1 = 18
        expected_result2 = 30

        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_non_numeric_characters(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding(["1, 2, qwerty3"])

        output = mock_stdout.getvalue().strip()

        expected_result = "I can't do it"

        self.assertEqual(output, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_fractional_numbers(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding(["1, 2, 1.5"])

        output = mock_stdout.getvalue().strip()

        expected_result = "I can't do it"

        self.assertEqual(output, expected_result)

    # Negative
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_list(self, mock_stdout):
        splitting_string_list_to_numbers_and_adding([""])

        output = mock_stdout.getvalue().strip()

        expected_result = "I can't do it"

        self.assertEqual(output, expected_result)


class ArithmeticMeanTest(unittest.TestCase):
    def test_arithmetic_mean_positive(self):
        result = the_arithmetic_mean_of_the_list([1, 5, 10, 4])

        expected_result = 5

        self.assertEqual(result, expected_result)

    def test_arithmetic_mean_negative(self):
        result = the_arithmetic_mean_of_the_list([-1, -5, -10, -4])

        expected_result = -5

        self.assertEqual(result, expected_result)

    def test_arithmetic_mean_negative_and_positive(self):
        result = the_arithmetic_mean_of_the_list([-1, 5, 10, -4])

        expected_result = 2.5

        self.assertEqual(result, expected_result)

    def test_arithmetic_mean_single_number(self):
        result = the_arithmetic_mean_of_the_list([10])

        expected_result = 10

        self.assertEqual(result, expected_result)

    def test_arithmetic_mean_zero(self):
        result = the_arithmetic_mean_of_the_list([0])

        expected_result = 0

        self.assertEqual(result, expected_result)

    # Negative
    def test_arithmetic_mean_non_numeric(self):
        with self.assertRaises(TypeError):
            the_arithmetic_mean_of_the_list(["qwerty1"])

    def test_arithmetic_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            the_arithmetic_mean_of_the_list([])


if __name__ == '__main__':
    unittest.main(verbosity=3)
