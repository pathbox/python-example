from collections.abc import *


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):  # 判断ele是否可迭代
            flatten(ele, output_arr)  # 尾数递归
        else:  # 不是Iterable则加到输出output_arr中
            output_arr.append(ele)
    return output_arr


print(flatten([[1, 2, 3], [4, 5]], [6, 7]))
