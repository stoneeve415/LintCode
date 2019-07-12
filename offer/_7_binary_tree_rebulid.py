# -*- coding: utf-8 -*-
"""
@title: 重建二叉树
@author: evestone
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def buildTree(inorder, postorder):
    # write your code here
    if not inorder:
        return None
    rootPos = inorder.index(postorder[-1])
    root = TreeNode(postorder[-1])
    root.left = buildTree(inorder[:rootPos], postorder[:rootPos])
    root.right = buildTree(inorder[rootPos + 1:], postorder[rootPos:-1])
    return root

def buildTree(preorder, inorder):
    # write your code here
    if not inorder:
        return None
    rootPos = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:rootPos+1], inorder[:rootPos])
    root.right = buildTree(preorder[rootPos+1:], inorder[rootPos + 1:])
    return root