# -*- coding: utf-8 -*-
"""
@title: 最小的k个数
@author: evestone
"""

def getLeastNum(arr, start, end, k):
    if start >= end:
        return
    left, right = start, end
    temp = arr[left]
    while left < right:
        while left < right and arr[right] > temp:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        while left < right and arr[left] <= temp:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left] = temp
    getLeastNum(arr, start, left-1, k)
    if left < k-1:
        getLeastNum(arr, left+1, end, k)


if __name__ == '__main__':
    arr = [4, 5, 1, 6, 2, 7, 3, 8, 1]
    k = 5
    getLeastNum(arr, 0, 8, 4)
    print(arr[:k])