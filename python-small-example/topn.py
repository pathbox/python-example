from heapq import nlargest


def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])


print(topn_dict({'a': 10, 'b': 8, 'e': 3, 'c': 9, 'd': 10}, 3))
