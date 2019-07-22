# -*- coding: utf-8 -*-
"""
@title: 斐波拉西数列
@author: evestone
"""

'''
相关题目：青蛙跳台阶，小矩形覆盖大矩形
'''

def fabonacci(n):
    x, y = 0, 1
    for i in range(n-1):
        x, y = y, x+y
    return y


if __name__ == '__main__':
    n = 9
    print(fabonacci(n))