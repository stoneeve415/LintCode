# -*- coding: utf-8 -*-
"""
@title: 1671 玩游戏
@author: evestone
"""


def playGames(A):
    _max = max(A)
    left, right = 0, _max*2
    while left < right:
        mid = (left+right) // 2
        cnt = 0
        for item in A:
            cnt += max(mid-item, 0)
        if mid > cnt:
            left = mid + 1
        else:
            right = mid
    return max(left, _max)


if __name__ == '__main__':
    # A = [84, 53]
    A = [2, 2, 4, 3]
    print(playGames(A))