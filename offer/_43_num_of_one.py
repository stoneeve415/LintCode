# -*- coding: utf-8 -*-
"""
@title: 1-n中1出现的次数
@author: evestone
"""

def numOfOne(n):
    if n < 1:
        return 0
    count = 0
    base = 1
    round = n
    while round > 0:
        weight = round % 10
        round = round // 10
        count += round*base
        if weight == 1:
            count += n % base + 1
        elif weight > 1:
            count += base
        base *= 10
    return count


if __name__ == '__main__':
    n = 11
    print(numOfOne(n))
