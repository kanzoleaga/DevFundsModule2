import unittest
from src.com.jalasoft.search_files.utils.validator import *

class ValidatorTest(unittest.TestCase):
    def test_is_number_is_true_for_cero(self):
        self.assertTrue(is_number(0))

    def test_is_number_is_false_for_strings(self):
        self.assertFalse(is_number('hello'))

    def test_is_positive_is_true_for_a_number_greater_than_cero(self):
        self.assertTrue(is_posiive(456))

    def test_is_positive_is_false_for_a_number_minnor_than_cero(self):
        self.assertFalse(is_posiive(-25))

    def test_is_positive_is_false_for_a_string(self):
        self.assertFalse(is_posiive('negative'))

    def test_is_in_range_returns_true_for_a_value_between_down_and_up_limits(self):
        self.assertTrue(is_in_range(5, 2, 8))

    def test_is_in_range_returns_false_for_a_value_NOT_between_down_and_up_limits(self):
        self.assertFalse(is_in_range(16, 0, 6))

    def test_is_in_range_raises_an_exception_when_one_or_more_argumets_are_not_integers(self):
        with self.assertRaises(ValueError):
            is_in_range(2, '1', 'nine')

