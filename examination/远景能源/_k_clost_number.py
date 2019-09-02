# -*- coding: utf-8 -*-
"""
@title: 求排序数组中最靠近x的k个数
@author: evestone
"""

import sys
# 二分查找
def binarySearch(nums, target):
    # write your code here
    left, right = 0, len(nums)-1
    if right == -1:
        return -1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    return left

# 判断是否选择左边left那个数
def isClost(arr, x, left, right):
    if left < 0:
        return False
    if right > len(arr)-1:
        return True
    if x - arr[left] <= arr[right] - x:
        return True
    return False

# 查找最近k个数
def kClost(arr, k, x):
    if arr is None or len(arr) == 0:
        return None
    left = binarySearch(arr, x)
    right = left + 1
    res = []
    for i in range(k):
        if isClost(arr, x, left, right):
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1
    return sorted(res)


if __name__ == '__main__':

    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = 3
    # print(kClost(arr, k, x))
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    arr = list(map(int, line.split(',')))
    k = int(sys.stdin.readline().strip())
    x = int(sys.stdin.readline().strip())
    print(kClost(arr, k, x))