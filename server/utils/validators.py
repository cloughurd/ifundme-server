def is_positive_number(x):
    if not (isinstance(x, float) or isinstance(x, int)):
        return False
    if x > 0:
        return True
    return False
