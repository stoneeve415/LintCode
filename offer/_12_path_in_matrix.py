# -*- coding: utf-8 -*-
"""
@title: 矩阵中路径
@author: evestone
"""


def hasPath(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    _len = len(target)
    visit = [[False]*n]*m

    def check(row, col, cur_len):
        if cur_len == _len:
            return True
        res = False
        if 0 <= row < m and 0 <= col < n and \
                matrix[row][col] == target[cur_len] and not visit[row][col]:
            cur_len += 1
            visit[row][col] = True
            res = check(row, col-1, cur_len) or check(row-1, col, cur_len) or \
                check(row, col + 1, cur_len) or check(row+1, col, cur_len)
            if not res:
                cur_len -= 1
                visit[row][col] = False
        return res

    for row in range(m):
        for col in range(n):
            if check(row, col, 0):
                return True

    return False


if __name__ == '__main__':
    matrix = [['a', 'b', 't', 'g'],
              ['c', 'f', 'c', 's'],
              ['j', 'd', 'e', 'h']]
    target = ['b', 'f', 'c', 'e']
    print(hasPath(matrix, target))
