# -*- coding: utf-8 -*-
"""
@title: 392.534.535 房屋打劫
@author: evestone
"""


# 房屋连成一条线，打劫最大价值
def houseRobber(A):
    # write your code here
    n = len(A)
    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    dp = [0] * (n + 1)
    dp[1] = A[0]
    dp[2] = max(A[0], A[1])
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 2] + A[i - 1], dp[i - 1])
    return dp[n]


# 房屋连成一个圈，打劫最大价值（插头去尾求最大值）
def houseRobber2(nums):
    # write your code here
    # write your code here
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0], dp[1] = 0, nums[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    answer = dp[n - 1]

    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, n - 1):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return max(dp[n - 2], answer)


# 房屋连成一棵二叉树，打劫最大价值
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def houseRobber3(self, root):
    # write your code here
    def dfs(root):
        if root is None:
            return 0, 0

        left_rob, left_not_rob = dfs(root.left)
        right_rob, right_not_rob = dfs(root.right)
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob

    rob, not_rob = dfs(root)
    return max(rob, not_rob)


if __name__ == '__main__':
    A = [3, 4, 5]
    print(houseRobber(A))
    print(houseRobber2(A))