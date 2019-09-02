# -*- coding: utf-8 -*-
"""
@title: 股票的最大利润
@author: evestone
"""


def maxStock(arr):
    if arr is None or len(arr) < 2:
        return 0
    _min = min(arr[0], arr[1])
    maxDiff = arr[1]-arr[0]
    for i in range(2, len(arr)):
        if arr[i-1] < _min:
            _min = arr[i-1]
        curDiff = arr[i]-_min
        if curDiff > maxDiff:
            maxDiff = curDiff
    return maxDiff



if __name__ == '__main__':
    arr = [9, 11, 8, 5, 7, 12, 16, 14]
    print(maxStock(arr))