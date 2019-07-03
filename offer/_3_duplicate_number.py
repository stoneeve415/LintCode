# -*- coding: utf-8 -*-
"""
@title: 0-n 重复数字
@author: evestone
"""


# 方法一：哈希 O(n) O(n)
def duplicateNumber(nums):
    mhash = {}
    res = []
    for item in nums:
        if item in mhash:
            if mhash[item]:
                res.append(item)
                mhash[item] = False
        else:
            mhash[item] = True
    return res


# 方法一：交换 O(n) O(1)
def duplicateNumber2(a):
    res = set()
    for i in range(len(a)):
        while a[i] != i:  # 非常关键，当这个条件满足时，一直执行，直到不满足为止
            if a[a[i]] == a[i]:
                res.add(a[i])
                break
            else:
                a[a[i]], a[i] = a[i], a[a[i]]  # 目标是遍历交换使得a[a[i]] == a[i]成立，返回a[i],一定可以找到，所以不会是死循环
    return res


if __name__ == '__main__':
    arr = [2, 3, 1, 0, 2, 5, 3, 3]
    print(duplicateNumber(arr))
    print(duplicateNumber2(arr))
