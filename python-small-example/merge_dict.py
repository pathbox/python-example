from collections.abc import Iterable


def merge_dict(dict1, dict2):
    c = dict1.copy()
    c.update(dict2)
    return c


def merge_dict2(dic1, dic2):
    return {**dic1, **dic2}


r = merge_dict({'a': 1, 'b': 2}, {'c': 3})
print(r)

r = merge_dict2({'a': 1, 'b': 2}, {'c': 3})
print(r)
