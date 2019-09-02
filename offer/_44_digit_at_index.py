# -*- coding: utf-8 -*-
"""
@title: 数字序列中某一位的数字
@author: evestone
"""


# 求num位数占多少位置
def countOfInt(num):
    if num == 1:
        return 10
    else:
        return 9 * int(pow(10, num-1)) * num


def digitAtIndex(n):
    if n < 10:
        return n-1
    base = 1
    while True:
        if n < countOfInt(base):
            break
        n -= countOfInt(base)
        base += 1
    start = int(pow(10, base - 1))
    # 表示第round个base位数
    round = n // base
    # 表示第round个base位数的第几位
    weight = n % base
    num = start + round
    return num // int(pow(10, (base-weight-1))) % 10


if __name__ == '__main__':
    n = 1001
    print(digitAtIndex(n))