import unittest
from src.com.jalasoft.search_files.search.search_criteria import *

class SearchCriteriaTest(unittest.TestCase):

    def test_search_criteria_constructor_raises_an_exception_for_invalid_path(self):
        with self.assertRaises(AttributeError):
            SearchCriteria.__init__(self,'C:\MyPython@#$#%dfhghR\sdfadTEST')
        #self.assertTrue('Invalid attribute path' in context.exception)
if __name__ == '__main__':
    unittest.main()