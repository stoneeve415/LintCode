# -*- coding: utf-8 -*-
"""
@title: 797. 到达一个数字
@author: evestone
"""

import math


def reachNumber(target):
    # Write your code here
    t = abs(target)
    n = int(math.ceil((-1.0 + math.sqrt(1 + 8.0 * t)) / 2))

    sum = n * (n + 1) // 2
    diff = sum - target
    if diff == 0:
        return n
    elif diff % 2 == 0:
        return n
    elif (diff + n + 1) % 2 == 0:
        return n + 1
    else:
        return n + 2