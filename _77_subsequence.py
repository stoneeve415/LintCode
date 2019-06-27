# -*- coding: utf-8 -*-
"""
@title: 77.762 最长公共子序列 76. 最长上升子序列 397.398 最长上升连续子序列 191. 乘积最大子序列

@author: evestone
"""


'''
最长公共子序列
'''


def longestCommonSubsequence(A, B):
    # write your code here
    l1, l2 = len(A), len(B)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[l1][l2]


def longestCommonSubsequence2(P, Q, k):
    # Write your code here
    l1, l2 = len(P), len(Q)
    dp = [[[0] * (k + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if P[i - 1] == Q[j - 1]:
                dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])
            for u in range(1, k + 1):
                if P[i - 1] == Q[j - 1]:
                    dp[i][j][u] = dp[i - 1][j - 1][u] + 1
                else:
                    dp[i][j][u] = max(dp[i - 1][j][u], dp[i][j - 1][u], dp[i - 1][j - 1][u - 1] + 1)
    return dp[l1][l2][k]


'''
最长上升子序列
'''


def longestIncreasingSubsequence(nums):
    # write your code here
    n = len(nums)
    dp = [1] * (n + 1)
    dp[0] = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            if nums[j - 1] < nums[i - 1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


'''
最长上升连续子序列
'''


def longestIncreasingContinuousSubsequence1(A):
    # write your code here
    n = len(A)
    if n == 0:
        return 0
    ascending = [1] * n
    descending = [1] * n
    for i in range(1, n):
        if A[i] > A[i - 1]:
            ascending[i] = ascending[i - 1] + 1
        else:
            descending[i] = descending[i - 1] + 1
    return max(max(ascending), max(descending))


'''
乘积最大子序列
'''


def maxProduct(nums):
    # write your code here
    n = len(nums)
    min_p = [0] * (n)
    max_p = [0] * (n)
    min_p[0] = max_p[0] = nums[0]
    for i in range(1, n):
        if nums[i] > 0:
            min_p[i] = min(min_p[i - 1] * nums[i], nums[i])
            max_p[i] = max(max_p[i - 1] * nums[i], nums[i])
        else:
            min_p[i] = min(max_p[i - 1] * nums[i], nums[i])
            max_p[i] = max(min_p[i - 1] * nums[i], nums[i])
    return max(max_p)


if __name__ == '__main__':
    A = 'ABCD'
    B = 'EDCA'
    print(longestCommonSubsequence(A, B))

    P = [8, 3]
    Q = [1, 3]
    k = 1
    print(longestCommonSubsequence2(P, Q, k))

    nums = [9, 3, 6, 2, 7]
    print(longestIncreasingSubsequence(nums))

    A = [5, 4, 2, 1, 3]
    print(longestIncreasingContinuousSubsequence1(A))

    nums2 = [-1, 2, 4, 1]
    print(maxProduct(nums2))

