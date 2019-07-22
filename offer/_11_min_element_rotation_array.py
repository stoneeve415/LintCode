# -*- coding: utf-8 -*-
"""
@title: 旋转数组最小元素
@author: evestone
"""

def min_element(nums):
    n = len(nums)
    if n == 0:
        return -1
    left, right = 0, n-1
    while left+1 < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid
        else:
            right = mid
    return min(nums[left], nums[right])


if __name__ == '__main__':
    nums = [3, 4, 4, 5, 1, 1, 2]
    print(min_element(nums))
    