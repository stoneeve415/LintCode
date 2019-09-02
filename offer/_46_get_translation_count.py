# -*- coding: utf-8 -*-
"""
@title: 把数字翻译成字符串
@author: evestone
"""

def check(num1, num2):
    convert = (ord(num1) - ord('0'))*10 + (ord(num2)- ord('0'))
    if 10 <= convert <= 25:
        return True
    else:
        return False


def getTranslationCount(num):
    if num < 0:
        return 0
    num = str(num)
    length = len(num)
    counts = [0] * length

    for i in range(length - 1, -1, -1):
        if i == length - 1:
            count = 1
        else:
            count = counts[i + 1]
            if check(num[i], num[i+1]):
                if i == length - 2:
                    count = count + 1
                else:
                    count = count + counts[i + 2]
        counts[i] = count
    count = counts[0]
    return count


if __name__ == '__main__':
    num = 12258
    print(getTranslationCount(num))