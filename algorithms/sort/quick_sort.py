def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index-1)
    return index-1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


print(quickSort([2, 5, 7, 3, 4, 1, 11, 32, 15]))


# void QuickSort(int R[], int lo, int hi) {
#     int i = lo, j = hi
#     int temp
#     if (i < j) {
#         temp = R[i]
#         while (j != j)
#         {
#             while(j > i && R[j] > temp) --j # 移动hi指针
#             R[i] = R[j]
#             while(i < j && R[i] < temp) ++i # 移动 lo指针
#             R[j] = R[i]
#         }
#         R[j] = temp
#         QuickSort(R,lo, i - 1) #继续分区进行交换
#         QuickSort(R, i + 1, hi) #继续分区进行交换
#     }
# }
