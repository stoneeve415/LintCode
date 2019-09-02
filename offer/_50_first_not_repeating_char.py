# -*- coding: utf-8 -*-
"""
@title: 第一个只出现一次的字符
@author: evestone
"""

def firstChar(str):
    if len(str) == 0:
        return -1
    mhash = {}
    for item in str:
        if item in mhash:
            mhash[item] += 1
        else:
            mhash[item] = 1
    for key, value in mhash.items():
        if value == 1:
            return key
    return -1



import sys
if __name__ == '__main__':
    str = "abaccdeff"
    # print(firstChar(str))
    while True:
        arr = []
        line = sys.stdin.readline()
        if line == '\n':
            break
        n = int(line)
        for i in range(n):
            line = sys.stdin.readline().strip()
            tmp = list(map(int, line.split(" ")))
            arr.append(tmp)
        print(n, arr)