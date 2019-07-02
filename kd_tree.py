# -*- coding: utf-8 -*-
"""
@title: kd树实现
@author: evestone
"""
import sys
import numpy as np


class Node:
    def __init__(self, p, dim=0):
        self.parents = None
        self.left = None
        self.right = None
        self.val = p
        self.split_dim = dim


class KDTree:
    def __init__(self):
        self.root = None

    def create(self, points):
        if len(points) == 0:
            return
        if len(points) == 1:
            return Node(points[0])
        # 计算两个维度方差
        var1 = np.var(points[:, 0])
        var2 = np.var(points[:, 1])
        if var1 > var2:
            index = np.argsort(points[:, 0])
            dim = 0
        else:
            index = np.argsort(points[:, 1])
            dim = 1
        median = len(points) // 2
        current = Node(points[index[median]], dim)

        if self.root is None:
            self.root = current
        left_node = self.create(points[index[:median]])
        if left_node:
            current.left = left_node
            left_node.parents = current
        right_node = self.create(points[index[median+1:]])
        if right_node:
            current.right = right_node
            right_node.parents = current

        return current

    def l2(self, x, y):
        return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

    def search(self, target):
        mstack = []
        cur = self.root
        #搜索到叶子节点
        while cur:
            mstack.append(cur)
            dim = cur.split_dim
            if target[dim] <= cur.val[dim]:
                cur = cur.left
            else:
                cur = cur.right

        # 当前最小距离和最近点
        min_dist = sys.maxsize
        min_point = None
        while mstack:
            node = mstack.pop()
            dim = node.split_dim
            # 计算目标点到分割线的距离
            dist_secant = abs(target[dim] - node.val[dim])
            # 计算当前节点和目标节点的距离
            dist_closed = self.l2(node.val, target)
            if dist_closed < min_dist:
                min_dist = dist_closed
                min_point = node.val
            # 目标点到分割线距离小于最小距离，另一子节点存在更近节点
            if dist_secant < dist_closed:
                dim = node.split_dim
                if target[dim] <= node.val[dim]:
                    node = node.right
                else:
                    node = node.left
                if node:
                    mstack.append(node)
                while node:
                    if target[dim] <= node.val[dim]:
                        node = node.left
                    else:
                        node = node.right
                    if node:
                        mstack.append(node)


        return min_point


if __name__ == '__main__':
    # https://blog.csdn.net/tjy1220646144/article/details/45483935
    '''
                  (7, 2)
              /           \
          (5, 4)             (9,6)
          /     \           /
    (2, 3)      (4, 7)   (8,1)
    
    '''
    # points = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
    # x1 = [2.1, 3.1]
    # x2 = [2, 4.5]
    points = np.array([[6, 5], [1, -3], [-6, -5], [-4, -10],
                       [-2, -1], [-5, 12], [2, 13], [17, -12],
                       [8, -22], [15, -13], [10, -6], [7, 15], [14, 1]])
    x2 = [-1, -5]
    tree = KDTree()
    tree.create(points)
    print(tree.search(x2))
