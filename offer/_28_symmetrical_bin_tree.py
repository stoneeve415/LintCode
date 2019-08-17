# -*- coding: utf-8 -*-
"""
@title: 对称的二叉树
@author: evestone
"""


def isSymmetrical(root):
    if root is None:
        return True

    def dfs(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

    return dfs(root.left, root.right)