# -*- coding: utf-8 -*-
"""
@title: 二维数组查找
@author: evestone
"""


# 方法一：O(m+n)
def searchMatrix1(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    i, j = 0, n - 1
    while i <= m-1 and j >= 0:
        if target > matrix[i][j]:
            i += 1
        elif target < matrix[i][j]:
            j -= 1
        else:
            return True
    return False


# 方法二：二分查找 O(logm+logn)
def searchMatrix2(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    left, right = 0, m*n-1
    while left < right:
        mid = (left+right) // 2
        i = mid // n
        j = mid % n
        if matrix[i][j] > target:
            right = mid
        elif matrix[i][j] < target:
            left = mid
        else:
            return True
    if matrix[left // n][left % n] == target:
        return True
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 7
    print(searchMatrix1(matrix, target))
    print(searchMatrix2(matrix, target))