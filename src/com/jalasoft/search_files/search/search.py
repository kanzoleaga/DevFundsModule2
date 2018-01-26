from  src.com.jalasoft.search_files.search.directory import Directory

class Search(object):
    def __init__(self, base_path):
        self.base_path = base_path
        self.directory = Directory()

    def search_all_directories(self):
        self.directory.show_all_directories(self.base_path)

    def search_all_files(self):
        pass

    def search_by_filter(self):
        pass

    def search_file_by_extesion(self):
        pass

    def search_file_by_content(self):
        pass

    def search_less_than_size(self):
        pass

    def search_greater_than_size(self):
        pass

    def search_only_sub_directories(self):
        pass

    def search_deeped_files(self):
        pass

    def count_files(self):
        pass

if __name__ == "__main__":
    search = Search("C:\\Program Files")
    search.search_all_directories()