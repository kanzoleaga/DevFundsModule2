import unittest
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria

class SearchCriteriaTest(unittest.TestCase):

    def test_search_criteria_constructor_raises_an_exception_for_invalid_path(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/MyPython@#$#%dfhghR/sdfadTEST')
        self.assertTrue('Invalid attribute path' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_not_numeric_size(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', size='sdfd')
        print(context.exception)
        self.assertTrue('Invalid attribute size' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_invalid_create_date(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', create_date='2017-sdfd', create_date_less_than=True)
        print(context.exception)
        self.assertTrue('Invalid attribute create_date' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_invalid_modify_date(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', modify_date='2017-sdfd', modify_date_less_than=False )
        print(context.exception)
        self.assertTrue('Invalid attribute modify_date' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_invalid_last_access_date(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', last_access_date='sdf-2017-sdfd')
        print(context.exception)
        self.assertTrue('Invalid attribute last_access_date' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_invalid_asset_type(self):
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', asset_type ='folders')
        print(context.exception)
        self.assertTrue('Invalid attribute asset_type' in str(context.exception))

    def test_search_criteria_constructor_raises_an_exception_for_invalid_size_less_than(self):
        """
        size_less_than must be boolean
        :return:
        """
        with self.assertRaises(AttributeError) as context:
            SearchCriteria.__init__(self,'C:/', size_less_than='Yes')
        print(context.exception)
        self.assertTrue('Invalid attribute size_less_than' in str(context.exception))


