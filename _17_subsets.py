# -*- coding: utf-8 -*-
"""
@title: 17 18, 子集
@author: evestone
"""


"""
不含重复元素
"""


# 非递归实现
def subsets1_1(nums):
    # write your code here
    res = [[]]
    temp = res.copy()
    for item1 in sorted(nums):
        for item2 in res:
            temp.append(item2 + [item1])
        res = temp.copy()
    return res


# 递归实现
def subsets1_2(nums):
    def dfs(depth, start, temp):
        res.append(temp)
        if depth == len(nums):
            return
        for i in range(start, len(nums)):
            dfs(depth + 1, i + 1, temp + [nums[i]])

    nums.sort()
    res = []
    dfs(0, 0, [])
    return res


"""
含重复元素
"""


# 非递归实现
def subsets2_1(nums):
    # write your code here
    res = [[]]
    temp = res.copy()
    for item1 in sorted(nums):
        for item2 in res:
            current = item2 + [item1]
            # 重复元素添加判断
            if current not in res:
                temp.append(current)
        res = temp.copy()
    return res


# 递归实现
def subsets2_2(nums):
    def dfs(depth, start, temp):
        if temp not in res:
            res.append(temp)
        if depth == len(nums):
            return
        for i in range(start, len(nums)):
            dfs(depth + 1, i + 1, temp + [nums[i]])

    nums.sort()
    res = []
    dfs(0, 0, [])
    return res


if __name__ == '__main__':
    # a = [1]
    # b = []
    # print(a+b)
    print(subsets2_1([1, 2, 2]))
