# -*- coding: utf-8 -*-
"""
@title: 树的最大深度
@author: evestone
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def maxDepth(root):
    if root is None:
        return 0
    l_max = maxDepth(root.left) + 1
    r_max = maxDepth(root.right) + 1
    return max(l_max, r_max)


def isBalance(root):
    if root is None:
        return 0
    left = isBalance(root.left)
    # 先判断左子树是不是，如果左子树是平衡树，继续检查右子树，如果不是平衡树，直接返回-1层层跳出递归直到他的根节点
    if left == -1:
        return -1
    right = isBalance(root.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:  # 执行到这一步，说明左右子树都是平衡二叉树，在判断在整体是不是二叉树，不是返回-1
        return -1
    return max(left, right) + 1  # 如果子树是平衡二叉树，则返回子树的高度


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(maxDepth(root))
    print(isBalance(root) != -1)