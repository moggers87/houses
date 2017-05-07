def is_two_int_tuple(value):
    """Checks that value is 2-int tuple"""
    if not isinstance(value, tuple):
        return False
    elif len(value) != 2:
        return False
    else:
        return all([isinstance(i, int) for i in value])
