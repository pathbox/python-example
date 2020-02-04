"""
Given an array S of n integers, are there three distinct elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
1. 将数组排成有序数组，已经有序则不需要
2. 游标 i 以及 l r
3. 对于相邻游标重复不需要再算一遍的过滤
"""


def three_sum(array):
    """
      :param array: List[int]
      :return: Set[ Tuple[int, int, int] ]
      """
    res = set()
    array.sort()  # 先排序
    for i in range(len(array)-2):
        if i > 0 and array[i] == array[i-1]:  # 重复的数值一直移动 不需要再算一次
            continue
        l, r = i+1, len(array) - 1
        while l < r:
            s = array[i]+array[l]+array[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.add((array[i], array[l], array[r]))

                while l < r and array[l] == array[l+1]:  # 重复的数值一直移动
                    l += 1
                while l < r and array[r] == array[r - 1]:  # 重复的数值一直移动
                    r -= 1

                l += 1  # 现在真正的移动游标
                r -= 1  # 现在真正的移动游标
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
