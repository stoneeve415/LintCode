# -*- coding: utf-8 -*-
"""
@title: 出现次数超过一半的数字
@author: evestone
"""

def moreThanHalfNum(arr):
    mhash = {}
    for item in arr:
        if item in mhash:
            mhash[item] += 1
            if mhash[item] > len(arr) // 2:
                return item
        else:
            mhash[item] = 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(moreThanHalfNum(arr))