# -*- coding: utf-8 -*-
"""
@title: kd树实现
@author: evestone
"""
import numpy as np
class Node():
    def __init__(self, p):
        self.parents = None
        self.left = None
        self.right = None
        self.val = p


class KDTree():
    def __init__(self):
        self.root = None

    def create(self, points):
        if len(points) == 1:
            return Node(points[0])
        var1 = np.var(points[:, 0])
        var2 = np.var(points[:, 1])
        if var1 > var2:
            index = np.argsort(points[:, 0])
        else:
            index = np.argsort(points[:, 1])
        median = len(points) // 2
        current = Node(points[median])
        if self.root is None:
            self.root = current
        current.left = self.create(points[index[:median]])
        current.right = self.create(points[index[median+1:]])

        return current


    def search(self, x):
        pass


if __name__ == '__main__':
    points = np.array([[6, 2], [6, 3], [3, 5], [5, 0], [1, 2], [4, 9], [8, 1]])
    x = [1, 1]
    tree = KDTree()
    tree.create(points)
    print(tree.search(x))
