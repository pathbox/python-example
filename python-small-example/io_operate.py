import os


def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)


def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fillist  # 返回读取内容

# 写入文件信息


f = open(r"./test.txt", "w", encoding="utf-8")
print(f.write("测试文件写入"))
f.close

# example2
# a写入，文件存在，则在文件内容后追加写入，不存在则创建
f = open(r"./test.txt", "a", encoding="utf-8")
print(f.write("测试文件写入gogogoggo"))
f.close

# example3
# with关键字系统会自动关闭文件和处理异常
with open(r"./test.txt", "w") as f:
    f.write("hello world!")
