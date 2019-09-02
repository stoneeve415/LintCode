# -*- coding: utf-8 -*-
"""
@title: n个骰子点数
@author: evestone
"""

# 递归求解
class Solution1:
    def __init__(self):
        self.n = 0
        self.curSum = 0
        self.max_value = 6
        self.count = []

    def recursive(self, index):
        if index == 0:
            self.count[self.curSum-self.n] += 1
            return
        for i in range(1, self.max_value):
            self.curSum += i
            self.recursive(index-1)
            self.curSum -= i

    def probability(self, n):
        res = []
        self.n = n
        self.count = [0] * ((self.n - 1) * self.max_value + 1)
        self.recursive(self.n)
        for i in range(len(self.count)):
            res.append([i+self.n, self.count[i] / pow(self.max_value, self.n)])
        return res


class Solution2:
    def __init__(self):
        self.max_value = 6

    def probability(self, n):
        if n < 1:
            return []
        probability = []
        probability.append([0] * (6 * n + 1))
        probability.append([0] * (6 * n + 1))
        flag = 0
        ratio = []
        for i in range(1, 7):
            probability[flag][i] = 1

        for k in range(2, n + 1):
            for i in range(0, k):
                probability[1 - flag][i] = 0
            for i in range(k, 6 * k + 1):
                probability[1 - flag][i] = 0
                for j in range(1, min(i + 1, 7)):
                    probability[1 - flag][i] += probability[flag][i - j]

            flag = 1 - flag

        total = pow(6, n)
        for i in range(n, 6 * n + 1):
            ratio.append([i, probability[flag][i] / total])
        return ratio

    def probability2(self, n):
        if n < 1:
            return []
        res = []
        # dp[i][j]前i个骰子和为n的j的种数
        dp = [[0]*(n*self.max_value+1) for _ in range(n+1)]
        for i in range(1, self.max_value+1):
            dp[1][i] = 1
        for i in range(2, n+1):
            # 从i开始（前i个骰子最小值为i），到i*6结束（前i个骰子最大值为i*6）
            for j in range(i, i*self.max_value + 1):
                for k in range(1, self.max_value+1):
                    dp[i][j] += dp[i-1][max(0, j-k)]

        for i in range(n, n*self.max_value+1):
            res.append([i, dp[n][i] / pow(self.max_value, n)])
        return res


if __name__ == '__main__':
    solution = Solution1()
    res = solution.probability(3)
    print(res)
    solution = Solution2()
    res = solution.probability(3)
    print(res)
    res = solution.probability2(3)
    print(res)