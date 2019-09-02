# -*- coding: utf-8 -*-
"""
@title: 不使用for while 乘除实现1+2+3+4+。。。+n
@author: evestone
"""

M, N = 0, 0
class A:
    def __init__(self):
        global M, N
        M += 1
        N += M


    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


if __name__ == '__main__':
    n = 10
    arr = [A()for _ in range(n)]
    print(N)