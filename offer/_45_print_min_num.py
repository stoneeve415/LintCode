# -*- coding: utf-8 -*-
"""
@title: 把数组排成最小的数
@author: evestone
"""

def mCompare(num1, num2):
    str1 = str(num1) + str(num2)
    str2 = str(num2) + str(num1)
    if str1 > str2:
        return True
    else:
        return False


def qsort(arr, start, end):
    if start >= end:
        return
    left, right = start, end
    temp = arr[left]
    while left < right:
        while left < right and mCompare(arr[right], temp):
            right -= 1
        if left < right:
            arr[left] = arr[right]
        while left < right and not mCompare(arr[left], temp):
            left += 1
        if left < right:
            arr[right] = arr[left]
    arr[left] = temp
    qsort(arr, start, left)
    qsort(arr, left+1, end)


def printMinNum(arr):
    qsort(arr, 0, len(arr)-1)
    return ''.join(list(map(str,arr)))


if __name__ == '__main__':
    arr = [3, 32, 321]
    print(printMinNum(arr))