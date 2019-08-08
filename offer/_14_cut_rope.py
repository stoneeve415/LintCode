# -*- coding: utf-8 -*-
"""
@title: 剪绳子求最大乘积
@author: evestone
"""

def cutRope(n):
    dp = [1]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[j] = max(dp[j], dp[j-i]*i)
    return dp[n]


if __name__ == '__main__':
    n = 10
    print(cutRope(n))