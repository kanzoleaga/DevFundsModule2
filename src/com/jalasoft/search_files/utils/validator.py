import datetime
import os
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria

class Validator(object):

    def is_number(self, value):
        """
        Returns True if the argument is an integer
        :param value: int   The value to be evaluated
        :return: bool
        """
        try:
            int(value)
            return True
        except:
            return False

    def is_date_time(self,value):
        """
        Returns true if the value entered is a valid date
        :param value: Date
        :return: bool
        """
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return True
        except:
            return False

    def is_positive(self, value):
        """
        Returns True if the argument is a positive integer
        :param value: int   The value to be evaluated
        :return: bool
        """
        if self.is_number(value) and value >= 0:
            return True
        else:
            return False

    def is_in_range(self, value, down_limit, up_limit):
        """
        Returns True if the first argument is between down_limit and up_limit
        :param value: int   The value to be evaluated
        :param down_limit: int  Inferior limit
        :param up_limit: int    Superior limit
        :return: bool
        """
        if self.is_number(value) and self.is_number(down_limit) and self.is_number(up_limit):
            if down_limit <= value and value <= up_limit:
                return True
            else:
                return False
        else:
            raise ValueError ("One or more arguments is not an integer.")

    def is_valid_path(self, value):
        if not os.path.isdir(value):
            return False
        else:
            return True

    def is_valid_asset(self, value):
        if value != 'dir' and value != 'file':
            return False
        else:
            return True

    def is_bool(self, value):
        return isinstance(value, bool)

    def is_valid_criteria(self, criteria):
        if not isinstance(criteria, SearchCriteria):
            return False
        else:
            if criteria.get_crieria.value('path') is None:
                return False
            if (criteria.get_crieria.value('extension') is not None) \
                    and criteria.get_criteria_value('asset_type') == 'dir':
                return False
            if (criteria.get_crieria.value('owner') is not None) \
                    and criteria.get_criteria_value('asset_type') == 'dir':
                return False
            if (criteria.get_crieria.value('content') is not None) \
                    and criteria.get_criteria_value('asset_type') == 'dir':
                return False
        return True








