# -*- coding: utf-8 -*-
"""
@title: 打印从1到最大的n位数
@author: evestone
"""
res = []
nums = []
for i in range(10):
    nums.append(str(i))


def print_n(n):
    if n == 1:
        origin = []
        for i in range(1, 10):
            origin.append(str(i))
        res.extend(origin)
        return origin
    else:
        cur = []
        origin = print_n(n-1)
        for item in origin:
            for num in nums:
                cur.append(item+num)
        res.extend(cur)
        return cur


if __name__ == '__main__':
    n = 8
    print_n(n)
    print(len(res))
    print(res)

