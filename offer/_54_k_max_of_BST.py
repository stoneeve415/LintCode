# -*- coding: utf-8 -*-
"""
@title: 二叉搜索树第k大结点
@author: evestone
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def kMax(root, k):
    stack = []
    if root is None:
        return None
    i = 0
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        cur = stack.pop(-1)
        i += 1
        if i == k:
            return cur.val
        if cur.right:
            root = cur.right


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    k = 5
    print(kMax(root, k))
