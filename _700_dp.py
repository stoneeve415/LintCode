# -*- coding: utf-8 -*-
"""
@title: 700 动态规划问题
@author: evestone
"""

'''
杆子切割最大价值
'''


def cutting(prices, n):
    # Write your code here
    dp = [0] * (n + 1)
    for i in range(1, len(prices) + 1):
        for j in range(i, n + 1):
            dp[j] = max(dp[j], dp[j - i] + prices[i - 1])
    return dp[n]


if __name__ == '__main__':
    prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
    n1 = 8
    print(cutting(prices1, n1))
