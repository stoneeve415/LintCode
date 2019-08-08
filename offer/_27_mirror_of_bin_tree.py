# -*- coding: utf-8 -*-
"""
@title: 二叉树镜像
@author: evestone
"""


def Mirror(root):
    if root is None or (root.left is None and root.right is None):
        return root
    root.left, root.right = root.right, root.left
    if root.left:
        Mirror(root.left)
    if root.right:
        Mirror(root.right)
    return root

