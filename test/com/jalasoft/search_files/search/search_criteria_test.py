import unittest
from src.com.jalasoft.search_files.search.search_criteria import *

class SearchCriteriaTest(unittest.TestCase):

    def test_search_criteria_constructor_raises_an_exception_for_invalid_path(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:\MyPython@#$#%dfhghR\sdfadTEST')
        self.assertTrue('Invalid attribute path' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_not_numberic_size(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_create_date(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_modify_date(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_last_access_date(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_asset_type(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_create_date(self):
        pass

    def test_search_criteria_constructor_raises_an_exception_for_invalid_size_less_than(self):
        """
        size_less_than must be boolean
        :return:
        """
        pass
    
if __name__ == '__main__':
    unittest.main()