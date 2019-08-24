# -*- coding: utf-8 -*-
"""
@title: 二叉树的序列化和反序列化
@author: evestone
"""

class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None


res = []


def serialize(root):
    if root:
        res.append(root.value)
        serialize(root.left)
        serialize(root.right)
    else:
        res.append('$')

i = 0
def deserialize(arr):
    global i
    if arr[i] == '$':
        i += 1
        return None
    else:
        root = TreeNode(arr[i])
        i += 1
        root.left = deserialize(arr)
        root.right = deserialize(arr)
        return root

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    serialize(root)
    newR = deserialize(res)
    print(res)