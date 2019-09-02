# -*- coding: utf-8 -*-
"""
@title: 二分查找
@author: evestone
"""
# 数字在排序数组中出现的次数
def appearTimes(arr, num):
    if arr is None:
        return -1
    # 查找第一个k
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            if mid > 0 and arr[mid - 1] != num:
                first = mid
                break
            else:
                end = mid - 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    # 没找到num
    if start > end:
        return None

    # 查找最后一个k
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            if mid < len(arr)-1 and arr[mid+1] != num:
                last = mid
                break
            else:
                start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    # 没找到num
    if start > end:
        return None
    return last-first+1

# 0-n-1缺失的数
def missingNum(arr):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    if arr[left] == left:
        return left + 1
    else:
        return left


# 数组中数值和下标相等的元素
def equalElement(arr):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 3, 4, 5]
    num = 3
    print(appearTimes(arr, num))

    arr = [0, 1, 2, 3, 5, 6, 7]
    print(missingNum(arr))

    arr = [-3, -1, 1, 3, 5]
    print(equalElement(arr))