"""
@title: 26.搜索旋转矩阵
@author: evestone
"""


# 方法一
def search_min(A):
    i, j = 0, len(A)-1
    while i+1 < j:
        mid = (i+j)//2
        if A[mid] < A[j]:
            j = mid
        else:
            i = mid
    if A[i] < A[j]:
        return i
    else:
        return j


def bin_search(A, target):
    if len(A)== 0:
        return -1
    left, right = 0, len(A)-1
    while left+1 < right:
        mid = (left + right) // 2
        if A[mid] < target:
            left = mid
        else:
            right = mid
    if A[left] == target:
        return left
    elif A[right] == target:
        return right
    else:
        return -1


def search1(A, target):
    # write your code here
    if len(A)== 0:
        return -1
    min_i = search_min(A)
    left, right = 0, len(A)-1
    res1, res2 = bin_search(A[:min_i], target),bin_search(A[min_i:], target)
    if res1 != -1:
        return res1
    elif res2 != -1:
        return res2 + min_i
    else:
        return -1


# 方法二
def search2(A, target):
    # write your code here
    if len(A)== 0:
        return -1
    left, right = 0, len(A)-1
    while left+1 < right:
        mid = (left + right)//2
        if A[mid] >= A[left]:
            if target >= A[left] and target <= A[mid]:
                right = mid
            else:
                left = mid
        else:
            if target >= A[mid] and target <= A[right]:
                left = mid
            else:
                right = mid
    if A[left] == target:
        return left
    elif A[right] == target:
        return right
    return -1


if __name__ == '__main__':
    A = [6, 8, 9, 1, 3, 5]
    target = 5
    print(search1(A, target))
