# -*- coding: utf-8 -*-
"""
@title: 727. 中国剩余定理
@author: evestone
"""


def remainderTheorem(num, rem):
    # write your code here
    # writ your code here
    n = len(num)
    if n == 0:
        return 0
    x = rem[0] % num[0]
    # 最小公倍数
    com_multi = [1] * (n)
    com_multi[0] = num[0]
    for i in range(1, n):
        com_multi[i] = com_multi[i - 1] * num[i]

    for i in range(1, n):
        while x % num[i] != rem[i]:
            x += com_multi[i - 1]
        else:
            if i == n - 1:
                return x

    return 0


if __name__ == '__main__':
    # num = [3, 4, 5]
    # rem = [2, 3, 1]
    num = [23, 11, 29, 37, 31, 19, 17]
    rem = [12, 7, 8, 34, 13, 12, 3]
    print(remainderTheorem(num, rem))