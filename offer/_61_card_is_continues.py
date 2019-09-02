# -*- coding: utf-8 -*-
"""
@title: 扑克牌是否连续
@author: evestone
"""

def isContinue(arr):
    arr.sort()
    i = 0
    numOfZero = 0
    while arr[i] == 0:
        i += 1
        numOfZero += 1
    numOfGap = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            return False
        else:
            numOfGap += arr[i+1] - arr[i]-1
            i += 1
    return numOfGap <= numOfZero


if __name__ == '__main__':
    arr = [0, 1, 3, 4, 5]
    print(isContinue(arr))