# -*- coding: utf-8 -*-
"""
@title: 二叉树中和为某一值的路径
@author: evestone
"""

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def findPath(root, num):
    cur = []
    res = []

    def dfs(root, num):
        if root.left is None and root.right is None:
            if num == root.value:
                cur.append(root.value)
                res.append(cur.copy())
                cur.remove(root.value)
            return
        cur.append(root.value)
        dfs(root.left, num-root.value)
        dfs(root.right, num-root.value)
        cur.remove(root.value)

    dfs(root, num)
    return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    num = 22
    print(findPath(root, num))