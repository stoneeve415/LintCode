# -*- coding: utf-8 -*
import time
"""
@title: 92.125.440.562.563.564.798.799 背包问题
@author: evestone
"""

'''
求最大能装容量
'''


# 方法一：时间复杂度O(mn),空间复杂度O(mn)
def backPack1_1(m, A):
    # dp = [i][j] 前i个物品装入容量为j的背包中，能获取的最大值
    nums = len(A)
    if m == 0 or nums == 0:
        return 0
    dp = [[0]*(m+1) for i in range(nums+1)]
    for i in range(1, nums+1):
        for j in range(1, m+1):
            if A[i-1] <= j:
                dp[i][j] = max(dp[i-1][j-A[i-1]]+A[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[nums][m]


# 方法二：时间复杂度O(mn),空间复杂度O(m)
def backPack1_2(m, A):
    # write your code here
    nums = len(A)
    if m == 0 or nums == 0:
        return 0
    dp = [0]*(m+1)
    for i in range(1, nums+1):
        for j in range(m, A[i-1], -1):
            dp[j] = max(dp[j], dp[j-A[i-1]] + A[i-1]) # 第i个物品放或者不放

    return dp[m]


'''
求最大能装价值(不可重复取)
'''


# 方法一：时间复杂度O(mn),空间复杂度O(mn)
def backPack2_1(m, A, V):
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


# 方法二：时间复杂度O(mn),空间复杂度O(m)
def backPack2_2(m, A, V):
    nums = len(A)
    if m == 0 or nums == 0:
        return 0
    dp = [0]*(m+1)
    for i in range(1, nums+1):
        for j in range(m, A[i-1]-1, -1):
            dp[j] = max(dp[j], dp[j-A[i-1]] + V[i-1])
    return dp[m]


'''
求最大能装价值(可重复取)
'''


def backPack3(m, A, V):
    nums = len(A)
    dp = [0]*(m+1)
    for i in range(1, nums+1):
        for j in range(A[i-1], m+1):
            dp[j] = max(dp[j], dp[j-A[i-1]] + V[i-1])
    return dp[m]


'''
装满的种数
'''


# 可重复取，唯一排列
def backPack4(m, A):
    nums = len(A)
    dp = [0]*(m+1)
    for i in range(1, nums+1):
        for j in range(A[i-1], m+1):
            if A[i-1] == j:
                dp[j] += 1
            elif A[i-1] < j:
                dp[j] += dp[j-A[i-1]]
    return dp[m]


# 不可重复取
def backPack5(m, A):
    nums = len(A)
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(1, nums+1):
        for j in range(m, A[i-1]-1, -1):
            dp[j] += dp[j-A[i-1]]

    return dp[m]


# 可重复取 重复排列
def backPack6(m, A):
    nums = len(A)
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(1, m+1):
        for j in range(1, nums+1):
            if A[j-1] <= i:
                dp[i] += dp[i-A[j-1]]
    return dp[m]


'''
最大价值，物品添加数量限制
'''


def backPack7(n, prices, weight, amounts):
    # write your code here
    dp = [0] * (n + 1)
    _len = len(prices)
    for i in range(1, _len + 1):
        for _ in range(amounts[i - 1]):
            for j in range(n, prices[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - prices[i - 1]] + weight[i - 1])
    return dp[n]


'''
组合在1 ~ n范围内的值的数量
'''


def backPack8(n, value, amount):
    dp = [False] * (n + 1)
    result = 0
    dp[0] = True
    for i in range(0, len(value)):
        cnt = [0]*(n + 1)
        for j in range(value[i], n + 1):
            if not dp[j] and dp[j - value[i]] and cnt[j - value[i]] < amount[i]:
                dp[j] = dp[j - value[i]]
                result += 1
                cnt[j] = cnt[j - value[i]] + 1
    return result




if __name__ == '__main__':
    # m = 80000
    # A = [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932]
    # start = time.time()
    # print(backPack(m, A))
    # end = time.time()
    # print(end-start)
    #
    # start = time.time()
    # print(backPack2(m, A))
    # end = time.time()
    # print(end - start)

    # m2 = 10
    # A2 = [2, 3, 5, 7]
    # V2 = [1, 5, 2, 4]
    # print(backPack2_1(m2, A2, V2))
    # print(backPack2_2(m2, A2, V2))

    m3 = 10
    A3 = [2, 3, 5, 7]
    V3 = [1, 5, 2, 4]
    print(backPack3(m3, A3, V3))

    m4 = 7
    A4 = [2, 3, 6, 7]
    print(backPack4(m4, A4))

    m5 = 7
    A5 = [1, 2, 3, 3, 7]
    print(backPack5(m5, A5))

    m6 = 4
    A6 = [1, 2, 4]
    print(backPack6(m6, A6))

    n = 5
    value = [1,4]
    amount = [2,1]
    print(backPack8(n, value, amount))
