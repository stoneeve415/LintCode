# -*- coding: utf-8 -*-
"""
@title: 礼物的最大价值
@author: evestone
"""


# 递归
def maxGift1(arr, i , j):
    if i >= len(arr) or j >= len(arr[0]):
        return 0
    _max = max(maxGift1(arr, i, j+1), maxGift1(arr, i+1, j))
    return arr[i][j] + _max

# 循环
def maxGift2(arr):
    if arr is None:
        return 0
    m, n = len(arr), len(arr[0])
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            up, left = 0, 0
            if i > 0:
                up = dp[i-1][j]
            if j > 0:
                left = dp[i][j-1]
            dp[i][j] = arr[i][j] + max(up, left)
    return dp[m-1][n-1]


if __name__ == '__main__':
    arr =[[1, 10, 3, 8],
           [12, 2, 9, 6],
           [5, 7, 4, 11],
           [3, 7, 16, 5]]
    print(maxGift1(arr, 0, 0))
    print(maxGift2(arr))