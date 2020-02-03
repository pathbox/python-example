def limit(arr, min_lim=None, max_lim=None):
    def min_check(val): return True if min_lim is None else (min_lim <= val)
    def max_check(val): return True if max_lim is None else (val <= max_lim)

    return [val for val in arr if min_check(val) and max_check(val)]
