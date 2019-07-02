# -*- coding: utf-8 -*-
"""
@title: 1667 区间统计
@author: evestone
"""


# 求两端为0，中间1个数不大于k的区间个数
def intervalStatistics(arr, k):
    # Write your code here.
    n = len(arr)
    if n == 0:
        return 0

    left, right = 0, 0
    numOfOne, sum = 0, 0

    while right < n:
        if arr[right] == 1:
            numOfOne += 1
            right += 1
        elif arr[left] == 1:
            numOfOne -= 1
            left += 1
        else:
            while numOfOne > k:
                if arr[left] == 1:
                    numOfOne -= 1
                left += 1

            sum += right - left + 1 - numOfOne

            right += 1

    return sum


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 0, 1]
    k = 2
    print(intervalStatistics(arr, k))