# -*- coding: utf-8 -*-
"""
@title: 
@author: evestone
"""


def jump(n, m, target, d):

    def check(dis):
        cnt, last = 0, 0
        for i in range(n):
            if d[i] - last < dis:
                cnt += 1
            else:
                last = d[i]
        if cnt > m:
            return False
        return True
    d.append(target)
    left, right = 0, target
    while left <= right:
        mid = (left+right) // 2
        if check(mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


if __name__ == '__main__':
    # n = 5
    # m = 2
    # target = 25
    # d = [2, 11, 14, 17, 21]
    # print(jump(n, m, target, d))

    n = 0
    m = 0
    target = 10
    d = []
    print(jump(n, m, target, d))