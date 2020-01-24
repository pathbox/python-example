# 一键对多个值
from collections import defaultdict
d = {}
lst = [(1, 'apple'), (2, 'orange'), (1, 'compute')]
for k, v in lst:
    if k not in d:
        d[k] = []
    d[k].append(v)

print(d)  # {1: ['apple', 'compute'], 2: ['orange']}

# 使用defaultdict
d = defaultdict(list)
for k, v in lst:
    d[k].append(v)

# defaultdict(<class 'list'>, {1: ['apple', 'compute'], 2: ['orange']})
print(d)
