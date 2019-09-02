# -*- coding: utf-8 -*-
"""
@title: 构建乘积数组
@author: evestone
"""


def multiply(A):
    if not A:
        return []
    num = len(A)
    B = [None] * num
    # B[i]的意义是A数组不包括i位置的所有乘积，分为i左边的元素乘积和 i右边的所有元素乘积。
    # 初始化B[0]=1，是因为0左边没有元素，所以乘积为1。
    B[0] = 1
    for i in range(1, num):
        B[i] = B[i - 1] * A[i - 1]
    temp = 1
    for i in range(num - 2, -1, -1):  # 从后往前遍历不算最后一个（num-1）因为第一个for循环中已经计算了
        temp *= A[i + 1]
        B[i] *= temp

    return B


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(multiply(A))