import math


def mergeSort(arr):
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr)/2)  # 取中间为分区点
    left, right = arr[0:middle], arr[middle:]  # 得到左右两个数组
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:  # 不断的遍历 left right 比较，将当前较小的数放入result
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 处理剩下还有的数
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# mergeSort 不断的中间分区，merge 比较排序并合并,返回到上一层，继续比较排序合并直到最上层


print(mergeSort([2, 5, 7, 3, 4, 1, 11, 32, 15]))
