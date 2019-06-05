"""
@title: 65, 两个排序数组的中位数
@author: evestone
"""


# 方法一
def findMedianSortedArrays(A, B):
    len1 = len(A)
    len2 = len(B)
    length = len1 + len2
    mid = (length + 1) // 2
    current = mid + 1
    i, j = 0, 0
    temp = []
    while current > 0:
        if i < len1 and j < len2:
            if A[i] < B[j]:
                temp.append(A[i])
                i += 1
            else:
                temp.append(B[j])
                j += 1
        elif i < len1:
            temp.extend(A[i:i + current])
            break
        else:
            temp.extend(B[j:j + current])
            break
        current -= 1
    print(temp)
    print(mid)
    if length % 2 == 0:
        return (temp[mid - 1] + temp[mid]) / 2
    else:
        return temp[mid - 1]


# 方法二
def findMedianSortedArrays2(A, B):
    result = []
    while len(A) > 0 and len(B) > 0:
        if (A[0] > B[0]):
            result.append(B.pop(0))
        else:
            result.append(A.pop(0))
    if (len(A) > 0):
        result.extend(A)
    else:
        result.extend(B)
    pp = len(result) // 2
    if len(result) % 2 == 0:
        return (result[pp - 1] + result[pp]) / 2
    else:
        return result[pp]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    B = [2, 3, 4, 5]
    print(findMedianSortedArrays(A, B))