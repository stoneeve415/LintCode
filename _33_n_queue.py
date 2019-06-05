"""
@title: 33 34, n皇后
@author: evestone
"""


# 递归实现
def solver(n):
    checkerboard = [['.']*n for i in range(n)]
    check = [[True]*n for i in range(n)]
    res = []

    def is_occupied(row, col):
        for k in range(row):
            # top
            if not check[k][col]:
                return True
            # left top
            if k+col-row >= 0 and not check[k][k+col-row]:
                return True
            # right top
            if -k+col+row < n and not check[k][-k+col+row]:
                return True

        return False

    def recursive(checkerboard, k):
        if k == n:
            tmp = []
            for item in checkerboard:
                tmp.append(''.join(item))
            res.append(tmp)
            return
        # the k row
        for i in range(n):
            if not is_occupied(k, i):
                checkerboard[k][i] = 'Q'
                check[k][i] = False
                recursive(checkerboard, k+1)
            checkerboard[k][i] = '.'
            check[k][i] = True

    recursive(checkerboard, 0)
    return res


# 非递归实现
def solver2(n):
    checkerboard = [['.']*n for i in range(n)]
    check = [[True]*n for i in range(n)]
    res = []

    # if current place has been occupied
    def is_occupied(row, col):
        for k in range(row):
            # top
            if not check[k][col]:
                return True
            # left top
            if k+col-row >= 0 and not check[k][k+col-row]:
                return True
            # right top
            if -k+col+row < n and not check[k][-k+col+row]:
                return True
        return False

    stack = []
    k, i = 0, 0
    while True:
        # find all result and exit
        if k == 0 and i == n:
            break
        # find a place to put Queue
        if i < n and not is_occupied(k, i):
            checkerboard[k][i] = 'Q'
            check[k][i] = False
            stack.append((k, i))
            # next row
            k += 1
            i = 0
        else:
            i += 1
        if i >= n:  # current row cannot find a proper place
            #  Backtracking
            k, i = stack.pop(-1)
            checkerboard[k][i] = '.'
            check[k][i] = True
            i += 1
        if k == n:  # get the result
            tmp = []
            for item in checkerboard:
                tmp.append(''.join(item))
            res.append(tmp)
            #  Backtracking
            k, i = stack.pop(-1)
            checkerboard[k][i] = '.'
            check[k][i] = True
            i += 1
    return res


# 求数量
def solver_nums(n):
    checkerboard = [['.']*n for i in range(n)]
    check = [[True]*n for i in range(n)]
    res = 0

    def is_occupied(row, col):
        # top
        for k in range(row):
            if not check[k][col]:
                return True
        # left top
        for k in range(col):
            if not check[k+row-col][k]:
                return True
        # right top
        for k in range(col, n):
            if not check[row+col-k][k]:
                return True
        return False

    def recursive(checkerboard, k):
        nonlocal res
        if k == n:
            res += 1
            return
        # the k row
        for i in range(n):
            if not is_occupied(k, i):
                checkerboard[k][i] = 'Q'
                check[k][i] = False
                recursive(checkerboard, k+1)
            checkerboard[k][i] = '.'
            check[k][i] = True

    recursive(checkerboard, 0)
    return res


if __name__ == '__main__':
    print(solver2(1))
    # print(solver(4))
    # print(solver_nums(4))
    # print(solveNQueens1(4))

