# -*- coding: utf-8 -*-
"""
@title: 机器人运动范围
@author: evestone
"""


def robotPlay(m, n, k):
    visit = [[False] * n for _ in range(m)]

    def check(x, y):
        if 0 <= x < m and 0 <= y < n and not visit[x][y]:
            _sum = 0
            while x != 0 or y != 0:
                _sum += (x % 10 + y % 10)
                x /= 10
                y /= 10
            if _sum <= k:
                return True
        return False

    def dfs(x, y):
        if check(x, y):
            visit[x][y] = True
            return 1 + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1)
        else:
            return 0
    return dfs(0, 0)


if __name__ == '__main__':
    m = 20
    n = 20
    k = 18
    print(robotPlay(m, n , k))
