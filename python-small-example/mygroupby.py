from itertools import groupby
from operator import itemgetter
a = [{'date': '2019-12-15', 'weather': 'cloud'},
     {'date': '2019-12-13', 'weather': 'sunny'},
     {'date': '2019-12-14', 'weather': 'cloud'}]


a.sort(key=itemgetter('weather', 'date'))  # 根据date 排序
for k, items in groupby(a, key=itemgetter('weather')):
    print(k)
    for i in items:
        print(i)
