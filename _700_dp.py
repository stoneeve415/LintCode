# -*- coding: utf-8 -*-
"""
@title: 700.669 动态规划问题
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


'''
换硬币
'''


def coinChange(coins, amount):
    # write your code
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j == coins[i - 1]:
                dp[j] = 1
            elif j > coins[i - 1]:
                if dp[j - coins[i - 1]] != -1:
                    if dp[j] != -1:
                        dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
                    else:
                        dp[j] = dp[j - coins[i - 1]] + 1

    return dp[amount]


'''
卡牌游戏
'''


def cardGame(cost, damage, totalMoney, totalDamage):
    # Write your code here
    dp = [0] * (totalMoney + 1)
    for i in range(1, len(cost) + 1):
        for j in range(totalMoney, cost[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - cost[i - 1]] + damage[i - 1])
            if dp[totalMoney] >= totalDamage:
                return True
            else:
                return False


if __name__ == '__main__':
    prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
    n1 = 8
    print(cutting(prices1, n1))

    coins2 = [5, 2, 1]
    amount2 = 11
    print(coinChange(coins2, amount2))

    cost3 = [1, 2, 3, 4, 5]
    damage3 = [1, 2, 3, 4, 5]
    totalMoney3 = 10
    totalDamage3 = 10
    print(cardGame(cost3, damage3, totalMoney3, totalDamage3))

