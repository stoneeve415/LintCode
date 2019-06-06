# -*- coding: utf-8 -*-
"""
@title: 517.4.518 丑数
@author: evestone
"""
import sys


# 是否为丑数
def isUgly(num):
    # write your code here
    if num == 1:
        return True
    if num == 0:
        return False
    while num % 2 == 0:
        num = num // 2
        if num == 1:
            return True
    while num % 3 == 0:
        num = num // 3
        if num == 1:
            return True
    while num % 5 == 0:
        num = num // 5
        if num == 1:
            return True
    return False


# 动态规划实现
def nthUglyNumber(n):
    # write your code here
    dp = [0] * (n)
    dp[0] = 1
    a, b, c = 0, 0, 0
    for i in range(1, n):
        dp[i] = min(min(dp[a] * 2, dp[b] * 3), dp[c] * 5)
        if dp[i] / dp[a] == 2:
            a += 1
        if dp[i] / dp[b] == 3:
            b += 1
        if dp[i] / dp[c] == 5:
            c += 1
    return dp[n - 1]


# 给定质数集合的丑数
def nthSuperUglyNumber(n, primes):
    # write your code 
    dp = [0] * (n)
    dp[0] = 1
    windows = [0] * len(primes)
    for i in range(1, n):
        _min = sys.maxsize
        for j in range(len(primes)):
            if dp[windows[j]] * primes[j] < _min:
                _min = dp[windows[j]] * primes[j]
        dp[i] = _min
        for j in range(len(primes)):
            if dp[i] / dp[windows[j]] == primes[j]:
                windows[j] += 1
    return dp[n - 1]


if __name__ == '__main__':

    print(isUgly(4))
    print(nthUglyNumber(4))
    n = 11
    primes = [2, 3, 5]
    print(nthSuperUglyNumber(n, primes))