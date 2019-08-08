# -*- coding: utf-8 -*-
"""
@title: 调整数组顺序使奇数位于偶数前面
@author: evestone
"""

def reorder(arr):
    alen = len(arr)
    i, j = 0, alen-1
    while i < j:
        while i < j and arr[i] & 1 == 1:
            i += 1
        while i < j and arr[j] & 1 == 0:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [1, 3, 4, 56, 8, 6, 12, 5, 7]
    print(reorder(arr))