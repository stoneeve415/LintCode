# -*- coding: utf-8 -*-
"""
@title: 将二叉搜索树转化为双向链表
@author: evestone
"""


class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

head = None
tail = None
# 将二叉树转换为有序双向链表

def convert(root):
    global head, tail
    if root is None:
        return None
    convert(root.left)
    if head is None:
        head = root
        tail = root
    else:
        root.left = tail
        tail.right = root
        tail = root
    convert(root.right)
    return head


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    res = convert(root)
    a = 1
