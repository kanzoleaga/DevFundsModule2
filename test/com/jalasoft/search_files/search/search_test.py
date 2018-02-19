import unittest
import definition
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

    def test_satisfies_criteria_returns_true_if_the_size_is_greater_than_the_expected(self):
        """
        When size_less_than == false, the condition is 'greater or equal than'
        :return:
        """
        pass

    def test_satisfies_criteria_returns_true_if_the_size_is_equal_than_the_expected(self):
        """
        Regardless the value of size_less_than == false, the result will be true if the size is equal
        :return:
        """
        test_data_path = definition.ROOT_DIR+'\\test\\com\\jalasoft\\search_files\\utils\\test_data'
        file = File(test_data_path + '\\test_size_8kb.txt', 'test_size_8kb.txt')
        file.set_size()
        search = Search()
        # When criteria is less than size
        search.set_advanced_search_criteria(test_data_path, size=7508, size_less_than=True)
        self.assertTrue(search.satisfies_criteria(file))
        # When criteria is greater than size
        search.set_advanced_search_criteria(test_data_path, size=7508, size_less_than=False)
        self.assertTrue(search.satisfies_criteria(file))

        test_data_path = test_data_path + '\\test_dir'
        directory = Directory(test_data_path,'test_dir')
        directory.set_size()
        # When criteria is less than size
        search.set_advanced_search_criteria(test_data_path, size=25541, size_less_than=True)
        self.assertTrue(search.satisfies_criteria(directory))
        # When criteria is greater than size
        search.set_advanced_search_criteria(test_data_path, size=25541, size_less_than=False)
        self.assertTrue(search.satisfies_criteria(directory))

    def test_satisfies_criteria_returns_false_if_at_least_one_criteria_is_not_satisfied(self):
        pass

    def test_satisfies_criteria_returns_true_just_when_all_criteria_is_satisfied(self):
        pass


