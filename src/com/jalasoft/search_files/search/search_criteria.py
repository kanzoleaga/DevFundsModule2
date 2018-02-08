class SearchCriteria(object):
    def __init__(self, path, name, extension=None, asset_type=None, size=None, size_unit=None, owner=None,
                 create_date_range=None):

        """ **kwargs
        This is the constructor of the SearchCriteria class.
        Where size_range is a tuple (from_size, to_size)
        Where create_date_range is a tuple (from_date, to_date)
        Where asset_type is 'file' or 'dir'
        Where size_unit is either 'B', 'KB', 'MB', 'GB'
        :param path:
        :param name:
        :param extension:
        :param asset_type:
        :param size_range:
        :param size_unit:
        :param owner:
        :param create_date_range:
        """
        self.criteria = {
                        'path': path,
                        'name': name,
                        'extension': extension,
                        'asset_type': asset_type,
                        'size': size,
                        'size_unit': size_unit,
                        'owner': owner,
                        'create_date_range': create_date_range
        }


    def get_criteria_value(self, key):
        """
        This returns the value of an specific search criteria. For example it will return '.txt'
        in case the extension criteria has this value
        :param key: str the key name of the criteria
        :return:  the value of the criteria it may be an string or an integer
        """
        if key in self.criteria.keys():
            return self.criteria[key]
        else:
            raise ValueError('Invalid key. Key value' + key + 'is not a valid criteria')


