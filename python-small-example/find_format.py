import os


def find_file(work_dir, extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):  # 遍历当前目录文件
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1]  # 拿到扩展名
        if ext == '.' + extension:
            lst.append(filename)
    return lst


r = find_file('.', 'py')
print(r)
