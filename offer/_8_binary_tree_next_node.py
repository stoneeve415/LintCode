# -*- coding: utf-8 -*-
"""
@title: 二叉树的下一个节点
@author: evestone
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def inorderNext(root, target):
    if not root:
        return None
    if root.val == target.val:
        if not root.right:
            return None
        else:
            root = root.right
            while root.left:
                root = root.left
            return root
    if root.left and root.left.val == target.val:
        return root
    res1 = inorderNext(root.left, target)
    res2 = inorderNext(root.right, target)
    if res1:
        return res1
    elif res2:
        return res2
    else:
        return None


if __name__ == '__main__':
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right.left = TreeNode('f')
    root.right.right = TreeNode('g')
    root.left.right.left = TreeNode('h')
    root.left.right.right = TreeNode('i')
    target = TreeNode('e')
    next = inorderNext(root, target)
    if next:
        print(next.val)
    else:
        print(None)