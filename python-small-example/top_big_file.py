import os
from collections import namedtuple


def top_big_file(mydir, n=10):
    lst = []
    FileProp = namedtuple('FileProp', ['file_path', 'file_size'])
    for root, dirs, files in os.walk(mydir):
        for file in files:
            abs_path = os.path.join(root, file)
            si = os.stat(abs_path).st_size / 1024 / 1024  # MB
            fp = FileProp(abs_path, round(si, 3))
            lst.append(fp)

    lst = sorted(lst, key=lambda x: x.file_size,
                 reverse=True)  # 根据file_size倒序排序
    top10 = [x for i, x in enumerate(lst) if i < n]
    print(top10)


top_big_file('.')
