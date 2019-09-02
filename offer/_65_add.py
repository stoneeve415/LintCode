# -*- coding: utf-8 -*-
"""
@title: 不用加减乘除做加法
@author: evestone
"""

def mAdd(a, b):
    sum = 0
    while b:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return sum


if __name__ == '__main__':
    a = 1
    b = 11
    print(mAdd(a, b))