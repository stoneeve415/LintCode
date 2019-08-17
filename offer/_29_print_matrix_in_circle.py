# -*- coding: utf-8 -*-
"""
@title: 顺时针打印矩阵
@author: evestone
"""
res = []
def printMatrix(matrix, x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return
    if x1 == x2:
        for i in range(y1, y2 + 1):
            res.append(matrix[x1][i])
    elif y1 == y2:
        for i in range(x1, x2 + 1):
            res.append(matrix[i][y2])
    else:
        for i in range(y1, y2+1):
            res.append(matrix[x1][i])
        for i in range(x1+1, x2+1):
            res.append(matrix[i][y2])
        for i in range(y2-1, y1-1, -1):
            res.append(matrix[x2][i])
        for i in range(x2-1, x1, -1):
            res.append(matrix[i][y1])
        printMatrix(matrix, x1+1, y1+1, x2-1, y2-1)


if __name__ == '__main__':
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9],
    #           [10, 11, 12],
    #           [13, 14, 15]]


    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12]]

    # matrix = [[1, 2, 3, 4, 5],
    #           [6, 7, 8, 9,10],
    #           [11, 12, 13, 14, 15],
    #           [16, 17, 18, 19, 20]]


    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    M = len(matrix)
    N = len(matrix[0])
    printMatrix(matrix, 0, 0, M-1, N-1)
    print(res)
