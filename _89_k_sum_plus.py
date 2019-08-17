# -*- coding: utf-8 -*-
"""
@title: 89.90 k数之和
@author: evestone
"""


# 求k数之和方案的种数
def kSum(A, k, target):
    # write your code here
    n = len(A)
    # dp[i][j]:用i个数字得到和为j的种数
    dp = [[0] * (target + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for x in range(n):
        for i in range(k, 0, -1):
            for j in range(target, A[x] - 1, -1):
                dp[i][j] += dp[i - 1][j - A[x]]
    return dp[k][target]

# 求k数之和方案
def kSumII(A, k, target):
    # write your code here
    res = []
    cur = []

    def dfs(A, k, target, start):
        if k == 0:
            if target == 0:
                res.append(cur.copy())
            return
        if start > len(A) - 1:
            return
        for i in range(start, len(A)):
            tmp = A[i]
            cur.append(tmp)
            dfs(A, k - 1, target - tmp, i + 1)
            cur.remove(tmp)

    dfs(A, k, target, 0)
    return res


if __name__ == '__main__':
    A = [10,3,1,1]
    k = 3
    target = 5
    print(kSum(A, k, target))
    print(kSumII(A, k, target))