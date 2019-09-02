# -*- coding: utf-8 -*-
"""
@title: 和为s的数
@author: evestone
"""


# 和为s的两个数
def sum_k(arr, s):
    left, right = 0, len(arr)-1
    while left < right:
        if arr[left] + arr[right] < s:
            left += 1
        elif arr[left] + arr[right] > s:
            right -= 1
        else:
            return arr[left], arr[right]
    return -1, -1

# 和为s的连续正数序列
def positive_sum_s(s):
    res = []
    left, right = 1, 2
    cur_sum = left + right
    mid = max(4, (1+s) // 2)
    while left < mid:
        if cur_sum == s:
            res.append([left, right])
            cur_sum -= left
            left += 1
        elif cur_sum < s:
            right += 1
            cur_sum += right
        else:
            cur_sum -= left
            left += 1
    return res


if __name__ == '__main__':
    arr = [1, 2, 4, 7, 11, 15]
    print(sum_k(arr, 15))
    s = 15
    print(positive_sum_s(s))