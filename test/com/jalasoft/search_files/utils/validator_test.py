import unittest
from src.com.jalasoft.search_files.utils.validator import *

class ValidatorTest(unittest.TestCase):
    def test_is_number_is_true_for_cero(self):
        validator = Validator()
        self.assertTrue(validator.is_number(0))

    def test_is_number_is_false_for_strings(self):
        validator = Validator()
        self.assertFalse(validator.is_number('hello'))

    def test_is_positive_is_true_for_a_number_greater_than_zero(self):
        validator = Validator()
        self.assertTrue(validator.is_positive(456))

    def test_is_positive_is_false_for_a_number_minor_than_zero(self):
        validator = Validator()
        self.assertFalse(validator.is_positive(-25))

    def test_is_positive_is_false_for_a_string(self):
        validator = Validator()
        self.assertFalse(validator.is_positive('negative'))

    def test_is_in_range_returns_true_for_a_value_between_down_and_up_limits(self):
        validator = Validator()
        self.assertTrue(validator.is_in_range(5, 2, 8))

    def test_is_in_range_returns_false_for_a_value_NOT_between_down_and_up_limits(self):
        validator = Validator()
        self.assertFalse(validator.is_in_range(16, 0, 6))

    def test_is_in_range_raises_an_exception_when_one_or_more_arguments_are_not_integers(self):
        validator = Validator()
        with self.assertRaises(ValueError):
            validator.is_in_range(2, '1', 'nine')

    def test_is_valid_asset_returns_true_only_if_value_file_or_dir(self):
        validator = Validator()
        self.assertTrue(validator.is_valid_asset('file'))
        self.assertTrue(validator.is_valid_asset('dir'))
        self.assertFalse(validator.is_valid_asset('fileesd'))

    def test_is_date_time_returns_true_only_for_valid_dates(self):
        validator = Validator()
        self.assertTrue(validator.is_date_time('2018-01-01'))
        self.assertFalse(validator.is_date_time('201801011642'))

