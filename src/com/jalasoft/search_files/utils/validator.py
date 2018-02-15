import datetime

def is_number(value):
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

def is_date_time(value):
    """
    Returns true if the value entered is a valid date
    :param value: Date
    :return: bool
    """
    try:
        valid_date = datetime.datetime.strptime(value, '%Y-%m-%d-%H-%M')
        return True
    except ValueError:
        return False

def is_posiive(value):
    """
    Returns True if the argument is a positive integer
    :param value: int   The value to be evaluated
    :return: bool
    """
    if is_number(value) and value >= 0:
        return True
    else:
        return False

def is_in_range(value, down_limit, up_limit):
    """
    Returns True if the first argument is between down_limit and up_limit
    :param value: int   The value to be evaluated
    :param down_limit: int  Inferior limit
    :param up_limit: int    Superior limit
    :return: bool
    """
    if is_number(value) and is_number(down_limit) and is_number(up_limit):
        if down_limit <= value and value <= up_limit:
            return True
        else:
            return False
    else:
        raise ValueError ("One or more arguments is not an integer.")

