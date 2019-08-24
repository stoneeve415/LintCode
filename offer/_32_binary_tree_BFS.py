# -*- coding: utf-8 -*-
"""
@title: 层次遍历二叉树
@author: evestone
"""
class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None
res = []


# 层次遍历
def bfs(root):
    mQueue = []
    mQueue.append(root)
    while mQueue:
        for i in range(len(mQueue)):
            cur = mQueue[0]
            mQueue.pop(0)
            res.append(cur.value)
            if cur.left:
                mQueue.append(cur.left)
            if cur.right:
                mQueue.append(cur.right)


# 之字形层次遍历
def bfs_2(root):
    mStack1 = []
    mStack2 = []
    mStack1.append(root)
    while mStack1 or mStack2:
        if mStack1:
            for i in range(len(mStack1)):
                cur = mStack1[-1]
                mStack1.pop(-1)
                res.append(cur.value)
                if cur.left:
                    mStack2.append(cur.left)
                if cur.right:
                    mStack2.append(cur.right)

        if mStack2:
            for i in range(len(mStack2)):
                cur = mStack2[-1]
                mStack2.pop(-1)
                res.append(cur.value)
                if cur.right:
                    mStack1.append(cur.right)
                if cur.left:
                    mStack1.append(cur.left)


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    bfs_2(root)
    print(res)




