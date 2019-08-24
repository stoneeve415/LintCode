# -*- coding: utf-8 -*-
"""
@title: 判断是否为二叉搜索书的后序遍历
@author: evestone
"""


class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None


res = []

# 后序遍历
def last_order(root):
    mStack = []
    pre = None
    while root or mStack:
        while root:
            mStack.append(root)
            root = root.left
        cur = mStack[-1]
        if cur.right and cur.right != pre:
            root = cur.right
        else:
            res.append(cur.value)
            pre = cur
            mStack.pop(-1)


# 是否为二叉搜索树后序遍历
def is_last_order(arr, start, end):
    if start >= end:
        return True
    root  = arr[end]
    i = start
    while i <= end:
        if arr[i] > root:
            break
        i += 1
    if i == end:
        return is_last_order(start, end-1)
    mid = i
    while i <= end:
        if arr[i] < root:
            return False
        i += 1
    return is_last_order(arr, start, mid-1) and is_last_order(arr, mid, end-1)




if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    last_order(root)
    print(res)
    arr = [5, 7, 6, 9, 11, 10, 8]
    print(is_last_order(arr, 0, 6))
