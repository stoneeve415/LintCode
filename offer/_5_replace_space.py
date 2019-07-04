# -*- coding: utf-8 -*-
"""
@title: 替换空格
@author: evestone
"""


def replace(arr):
    cnt = 0
    for item in arr:
        if item == ' ':
            cnt += 1
    arr.extend(['#']*(cnt*2))
    n = len(arr)
    i, j = n-1-cnt*2, n-1
    while i >= 0:
        while i >= 0 and arr[i] != ' ':
            arr[j] = arr[i]
            i -= 1
            j -= 1
        if i >= 0:
            arr[j] = '0'
            arr[j-1] = '2'
            arr[j-2] = '%'
            j -= 3
            i -= 1
    return ''.join(arr)


if __name__ == '__main__':
    s = 'we are happy'
    arr = list(s)
    print(replace(arr))
