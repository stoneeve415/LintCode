# -*- coding: utf-8 -*-
"""
@title: 是否为弹栈顺序
@author: evestone
"""


# 第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序
def isPopList(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    if l1 != l2:
        return False
    i, j = 0, 0
    stack = []
    while i < l1:
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        else:
            if stack:
                if stack[-1] == arr2[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(arr1[i])
                    i += 1
            else:
                stack.append(arr1[i])
                i += 1
    while stack:
        if stack[-1] == arr2[j]:
            stack.pop()
            j += 1
        else:
            return False
    return True






if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 1, 2, 4, 3]
    # arr2 = [2, 1, 5, 4, 3]

    print(isPopList(arr1, arr2))