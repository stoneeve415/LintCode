"""
@title: 14 28 38.二分查找
@author: evestone
"""

'''
查找一维数组
'''


# 查找元素
def binarySearch(nums, target):
    # write your code here
    left, right = 0, len(nums)-1
    if right == -1:
        return -1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else :
            right = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    return -1


# 查找插入位置
def searchInsert(A, target):
    # write your code here
    left, right = 0, len(A) - 1
    if right == -1:
        return 0
    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid] < target:
            left = mid
        else:
            right = mid
    if A[left] >= target:
        return left
    elif A[right] >= target:
        return right
    else:
        return len(A)


'''
查找二维数组
'''


# 查找元素
def searchMatrix(matrix, target):
    # write your code here
    if len(matrix) == 0:
            return False
    row, col = len(matrix),len(matrix[0])
    left, right = 0, row*col-1
    while left + 1 < right:
        mid = (left + right) // 2
        mid_i = mid // col
        mid_j = mid % col
        if matrix[mid_i][mid_j] < target:
            left = mid
        else:
            right = mid
    if matrix[left//col][left%col] == target:
        return True
    elif matrix[right//col][right%col] == target:
        return True
    return False


# 查找并统计出现次数
def searchMatrixII(matrix, target):
    res = 0
    if len(matrix) == 0:
        return res
    row, col = len(matrix), len(matrix[0])
    i, j = row - 1, 0
    while i >= 0 and j < col:
        if matrix[i][j] == target:
            res += 1
            i -= 1
            j += 1
        elif matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target:
            i -= 1
    return res


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 7
    print(len(matrix), len(matrix[0]))
    print(searchMatrix(matrix, target))
