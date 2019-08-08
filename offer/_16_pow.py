# -*- coding: utf-8 -*-
"""
@title: 数值的整数次方
@author: evestone
"""

# 常规解法
def m_power(base, exp):
    res = 1
    flag = True
    if exp == 0:
        if base == 0:
            return 0
        return 1
    elif exp < 0:
        exp = -exp
        flag = False
    while exp:
        res *= base
        exp -= 1
    if not flag:
        res = 1/res

    return res


# 高效解法
def _power(base, exp):
    flag = True
    if exp == 0:
        if base == 0:
            return 0
        return 1
    elif exp < 0:
        exp = -exp
        flag = False
    res = _power(base, exp >> 1)
    res *= res
    if exp & 1 == 1:
        res *= base
    if not flag:
        res = 1 / res
    return res


if __name__ == '__main__':
    print(m_power(2.1, -2))
    print(m_power(2.1, -2))
