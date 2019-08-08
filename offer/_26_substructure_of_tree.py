# -*- coding: utf-8 -*-
"""
@title: 判断是不是树的结构
@author: evestone
"""


def isSubStructure(tree, sub):
    def hasSub(root1, root2):
        if sub is None:
            return True
        if root1 is None:
            return False
        if root1.value != root2.value:
            return False
        return hasSub(root1.left, root2.left) and hasSub(root1.right, root2.right)

    if tree.value == sub.value:
        res = hasSub(tree, sub)
    if not res:
        res = hasSub(tree.left, sub)
    if not res:
        res = hasSub(tree.right, sub)
    return sub



if __name__ == '__main__':
    pass