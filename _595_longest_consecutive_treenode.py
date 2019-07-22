# -*- coding: utf-8 -*-
"""
@title: 595 二叉树最长连续序列
@author: evestone
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 必须从父节点到子节点
def longestConsecutive(root):
    # write your code here
    if root is None:
        return 0
    _max = 1

    def dfs(root, cur_max):
        nonlocal _max
        if root is None:
            return
        if root.left and root.left.val == root.val + 1:
            left_max = cur_max + 1
            _max = max(_max, left_max)
            dfs(root.left, left_max)
        else:
            dfs(root.left, 1)

        if root.right and root.right.val == root.val + 1:
            right_max = cur_max + 1
            _max = max(_max, right_max)
            dfs(root.right, right_max)
        else:
            dfs(root.right, 1)

    dfs(root, 1)
    return _max



class Temp:
    def __init__(self, u=1, d=1):
        self.up = u
        self.down = d


def longestConsecutive2(root):
    # write your code here
    if root is None:
        return 0
    _max = 1

    def dfs(root):
        nonlocal _max
        up, down = 1, 1
        if root is None:
            return Temp(0, 0)
        left = dfs(root.left)
        right = dfs(root.right)
        if root.left:
            if root.left.val == root.val - 1:
                up = max(up, left.up + 1)
            if root.left.val == root.val + 1:
                down = max(down, left.down + 1)
        if root.right:
            if root.right.val == root.val - 1:
                up = max(up, right.up + 1)
            if root.right.val == root.val + 1:
                down = max(down, right.down + 1)
        _max = max(_max, up + down - 1)
        return Temp(up, down)

    dfs(root)
    return _max


if __name__ == '__main__':
    pass
