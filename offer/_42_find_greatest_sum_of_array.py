# -*- coding: utf-8 -*-
"""
@title: 连续子数组的最大和
@author: evestone
"""

def findGreatSum1(arr):
    if arr is None:
        return 0
    curSum = 0
    _max = -100
    for i in range(len(arr)):
        if curSum <= 0:
            curSum = arr[i]
        else:
            curSum += arr[i]
        if curSum > _max:
            _max = curSum
    return _max

# 动态规划
def findGreatSum2(arr):
    if arr is None:
        return 0
    dp = [0]*(len(arr)+1)
    dp[0] = 0
    for i in range(1, len(arr)):
        if dp[i-1] <= 0:
            dp[i] = arr[i]
        else:
            dp[i] = dp[i-1] + arr[i]
    return max(dp)


if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print(findGreatSum1(arr))
    print(findGreatSum2(arr))