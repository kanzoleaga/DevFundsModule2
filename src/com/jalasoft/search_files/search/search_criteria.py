from src.com.jalasoft.search_files.utils.validator import *

class SearchCriteria(object):


    def __init__(self, path, name=None, extension=None, asset_type=None, size=None, size_less_than=None,
                 owner=None, create_date=None, create_date_less_than=None, modify_date=None, modify_date_less_than=None,
                 last_access_date=None, content=None):

        """
        :param path: str This is the path where the searching is going to start. None is not supported
        :param name: str    This is the name of the file to be searched.
        :param extension: str  The extension of the file to be searched
        :param asset_type: str   The values accepted for this are file or dir
        :param size: int     The size in KB to be searched for
        :param size_less_than: bool  If False, files and directories greater than the size will be searched
        :param owner: str    The owner of the file
        :param create_date: datetime The creation date of the file
        :param modify_date: datetime The modification time of the file
        :param last_access_date: datetime. The last access date of the file
        :param content: str. The content to search in file
        """
        self.validator = Validator()
        if not self.validator.is_valid_path(path):
            raise AttributeError('Invalid attribute path')
        if asset_type is not None and not self.validator.is_valid_asset(asset_type):
            raise AttributeError('Invalid attribute asset_type')
        if size is not None and not self.validator.is_positive(size):
            raise AttributeError('Invalid attribute size')
        if size_less_than is not None and not self.validator.is_bool(size_less_than):
            raise AttributeError('Invalid attribute size_less_than')
        if create_date is not None and not self.validator.is_date_time(create_date):
            raise AttributeError('Invalid attribute create_date')
        if create_date_less_than is not None and not validator.is_bool(create_date_less_than):
            raise AttributeError('Invalid attribute create_date_less_than')
        if modify_date is not None and not validator.is_date_time(modify_date):
            raise AttributeError('Invalid attribute modify_date')
        if modify_date_less_than is not None and not validator.is_bool(modify_date_less_than):
            raise AttributeError('Invalid attribute modify_date_less_than')
        if last_access_date is not None and not validator.is_date_time(last_access_date):
            raise AttributeError('Invalid attribute last_access_date')
        else:
          self.criteria = {
                          'path': path,
                          'name': name,
                          'extension': extension,
                          'asset_type': asset_type,
                          'size': size,
                          'size_less_than': size_less_than,
                          'owner': owner,
                          'create_date': create_date,
                          'create_date_less_than': create_date_less_than,
                          'modify_date': modify_date,
                          'modify_date_less_than': modify_date_less_than,
                          'last_access_date': last_access_date,
                          'content': content
        }


    def get_criteria_value(self, key):
        """
        This returns the value of an specific search criteria. For example it will return '.txt'
        in case the extension criteria has this value
        :param key: str the key name of the criteria
        :return:  the value of the criteria it may be an string or an integer
        """
        logger.info("get_criteria_value : Enter")
        if key in self.criteria.keys():
            return self.criteria[key]
        else:
            raise ValueError('Invalid key. Key value' + key + 'is not a valid criteria')

