# -*- coding: utf-8 -*-
"""
@title: 91 最小调整代价
@author: evestone
"""


def min_adjust_cost(A, target):
    _len = len(A)
    _max = max(A) + target
    # 调整第i个数到j的最小代价
    dp = [[0]*(_max+1) for _ in range(_len+1)]
    for i in range(1, _len+1):
        for j in range(_max+1):
            left, right = max(j-target, 0), min(j+target, _max+target)
            dp[i][j] = min(dp[i-1][left:right+1]) + abs(A[i-1]-j)

    return min(dp[_len])


if __name__ == '__main__':
    A = [1, 4, 2, 3]
    target = 1
    print(min_adjust_cost(A, target))
