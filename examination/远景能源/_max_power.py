# -*- coding: utf-8 -*-
"""
@title: 给定发电站的距离和发电量数组和距离限制，求最大发电量
@author: evestone
"""

def maxPower(m, A, V):
    # dp = [i][j] 前i个物品装入容量为j的背包中，能获取的最大值
    nums = len(A)
    if m == 0 or nums == 0:
        return 0
    dp = [[0]*(m+1) for i in range(nums+1)]
    for i in range(1, nums+1):
        for j in range(1, m+1):
            if j >= A[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + V[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[nums][m]


if __name__ == '__main__':
    A = [30, 20, 35, 40]
    V = [20, 18, 25, 30]
    m = 50
    print(maxPower(m, A, V))


