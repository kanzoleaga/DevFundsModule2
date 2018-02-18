import unittest
from src.com.jalasoft.search_files.search.search import *

class SearchTest(unittest.TestCase):
    def test_satisfies_criteria_returns_false_if_the_asset_type_is_not_the_same(self):
        pass

    def test_satisfies_criteria_returns_true_if_the_asset_type_is_the_same(self):
        pass

    def test_satisfies_criteria_returns_false_if_the_extension_is_not_the_same(self):
        pass

    def test_satisfies_criteria_returns_true_if_the_extension_is_the_same(self):
        pass

    def test_satisfies_criteria_returns_false_if_the_size_is_not_less_than_the_expeced(self):
        pass

    def test_satisfies_criteria_returns_true_if_the_size_is_less_than_the_expeced(self):
        pass

    def test_satisfies_criteria_returns_false_if_the_size_is_not_greater_than_the_expeced(self):
        """
        When size_less_than == false, the condition is 'greater or equal than'
        :return:
        """
        pass

    def test_satisfies_criteria_returns_true_if_the_size_is_greater_than_the_expeced(self):
        """
        When size_less_than == false, the condition is 'greater or equal than'
        :return:
        """
        pass

    def test_satisfies_criteria_returns_true_if_the_size_is_equal_than_the_expeced(self):
        """
        Regardless the value of size_less_than == false, the result will be true if the size is equal
        :return:
        """
        pass




