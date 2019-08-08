# -*- coding: utf-8 -*-
"""
@title: 正则匹配
@author: evestone
"""

# 递归实现会超时
def regularMatch(pattern, target, i, j):
    if i == len(pattern) and j == len(target):
        return True
    elif i == len(pattern) or j == len(target):
        return False
    elif i < len(pattern)-1 and pattern[i+1] == '*':
        if pattern[i] == target[j] or pattern[i] == '.':
            return regularMatch(pattern, target, i+2, j+1) or \
                   regularMatch(pattern, target, i, j+1) or \
                   regularMatch(pattern, target, i+2, j)
        else:
            return regularMatch(pattern, target, i+2, j)
    else:
        if pattern[i] == target[j] or pattern[i] == '.':
            return regularMatch(pattern, target, i+1, j+1)
        else:
            return False


# 动态规划实现
def regularMatch2(pattern, target):
    plen, slen = len(pattern), len(target)
    dp = [[False]*(plen+1) for _ in range(slen+1)]
    # 前i个target和前j个pattern是否匹配
    dp[0][0] = True
    for i in range(2, plen+1):
        if pattern[i - 1] == '*':
            dp[0][i] = dp[0][i-2]
    for i in range(1, slen+1):
        for j in range(1, plen+1):
            if target[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                if target[i-1] != pattern[j-2] and pattern[j-2] != '.':
                    dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = dp[i][j-2] or dp[i-1][j]

    return dp[slen][plen]


if __name__ == '__main__':
    target = "aaaaaaaaaaaaab"
    pattern = "a*a*a*a*a*a*a*a*a*a*c"
    # print(regularMatch(pattern, target, 0, 0))
    print(regularMatch2(pattern, target))