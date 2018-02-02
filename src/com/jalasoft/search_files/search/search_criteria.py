class SearchCriteria(object):
    def __init__(self, criteria ):
        """
        This is the contructor of the SearchCriteria class.
        :param criteria: dic  the dictionary with keys as criterias to search
        The form of the criteria dictionaly is as follows:
        Where size_range is a tuple (from_size, to_size)
        Where create_date_range is a tuple (from_date, to_date)
        Where asset_type is 'file' or 'dir'
        """
        self.criteria = {
                        'path': criteria['path'],
                        'extension': criteria['extension'],
                        'name': criteria['name'],
                        'size_range': (criteria['size_range']),
                        'owner': criteria['owner'],
                        'create_date_range': criteria['create_date_range'],
                        'asset_type': criteria['asset_type']
        }

    def get_criteria_value(self, key):
        if key in self.criteria.keys:
            return self.criteria[key]
        else:
            raise ValueError('Invalid key. Key value' + key + 'is not a valid criteria')


criteria = {'path': 'c:\test', 
            'extension': '.txt'}
search_criteria = SearchCriteria(criteria)
print (extension = search_criteria.get_criteria_value('extension'))