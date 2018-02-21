import unittest
from src.com.jalasoft.search_files.search.search import *
from  src.com.jalasoft.search_files.search.directory import *
from  src.com.jalasoft.search_files.search.file import *
from src.com.jalasoft.search_files.search.search_criteria import *

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../resources")

class SearchTest(unittest.TestCase):

    def test_satisfies_criteria_for_directories(self):
        search = Search()
        search.set_basic_search_criteria(PATH, None, None, "dir")

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                self.assertFalse(search.satisfies_criteria(file))

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertTrue(search.satisfies_criteria(directory))

    def test_satisfies_criteria_for_files(self):
        search = Search()
        search.set_basic_search_criteria(PATH, None, None, "file")

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                self.assertTrue(search.satisfies_criteria(file))

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))

    def test_satisfies_criteria_for_file_extension(self):
        search = Search()
        search.set_basic_search_criteria(PATH, None, ".txt", "file")
        list_files = ["file04.txt", "fileA.txt", "file_I.txt"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_files)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))

    def test_satisfies_criteria_for_asset_name(self):
        search = Search()
        search.set_basic_search_criteria(PATH, "01", None, None)
        list_assets = ["file01.doc", "directory01"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_assets)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                if search.satisfies_criteria(directory):
                    self.assertTrue(directory.get_name() in list_assets)

    def test_satisfies_criteria_for_files_with_name_and_extension(self):
        search = Search()
        search.set_basic_search_criteria(PATH, "file", ".json", "file")
        list_files = ["file_III.json", "file03.json"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_files)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))

    def test_advanced_satisfies_criteria_file_size_less_than(self):
        search = Search()
        search.set_advanced_search_criteria(PATH, None, None, "file", 1, True, None, None,
                                            None, None, None, None, None)
        list_files = ["fileA.txt", "fileC.log"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_files)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))

    def test_advanced_satisfies_criteria_file_size_greater_than(self):
        search = Search()
        search.set_advanced_search_criteria(PATH, None, None, "file", 1, True, None, None,
                                            None, None, None, None, None)
        list_files = ["file01.doc", "file02.html", "file03.json", "file04.txt", "fileB.png", "file_I.txt",
                      "file_II.html", "file_III.json"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_files)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))

    def test_advanced_satisfies_criteria_files_modify_less_than_and_extension(self):
        search = Search()
        search.set_advanced_search_criteria(PATH, None, ".json", None, None, None, None, None, None,
                                            "2018-02-17", True, None, None)
        list_files = ["file03.json", "file_III.json"]

        for root, directories, files in os.walk(PATH):
            for file_name in files:
                file = File(os.path.join(root, file_name), file_name)
                if search.satisfies_criteria(file):
                    self.assertTrue(file.get_name() in list_files)

            for name in directories:
                directory = Directory(os.path.join(root, name), name)
                self.assertFalse(search.satisfies_criteria(directory))


