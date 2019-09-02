# -*- coding: utf-8 -*-
"""
@title: 翻转字符串
@author: evestone
"""

# 翻转单词顺序
def reverse(str):
    arr = str.split(' ')
    i, j = 0, len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return ' '.join(arr)

# 左转字符串
def leftRotate(str, num):
    str = list(str)
    left, mid= 0, num-1
    while left < mid:
        str[left], str[mid] = str[mid], str[left]
        left += 1
        mid -= 1
    mid, right = num, len(str)-1
    while mid < right:
        str[mid], str[right] = str[right], str[mid]
        mid += 1
        right -= 1

    left, right = 0, len(str)-1
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return ''.join(str)


if __name__ == '__main__':
    str = "i am a student."
    print(reverse(str))

    str2 = "abcdefg"
    num = 2
    print(leftRotate(str2, num))