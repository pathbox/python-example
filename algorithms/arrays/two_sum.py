"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""


def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            # target - num作为key,先存到dic,继续读取数组，只要之后有target - num值出现，则找到该配对
            dic[target - num] = i
    return None


print(two_sum([1, 1, 2, 7, 11, 15, 8, 2], 9))
