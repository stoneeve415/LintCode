# -*- coding: utf-8 -*-
"""
@title: 位运算 二进制中‘1’的个数
@author: evestone
"""


# 常规解法
def NumberOfOne(num):
    res = 0
    while num:
        if num % 2 == 1:
            res += 1
        num = num >> 1
    return res


# 新颖解法：该数减一后与原来数位于（将最右边的1变成0）
def NumberOfOnePlus(num):
    res = 0
    while num:
        res += 1
        num = num & (num-1)
    return res


if __name__ == '__main__':
    print(NumberOfOne(15))
    print(NumberOfOnePlus(15))

