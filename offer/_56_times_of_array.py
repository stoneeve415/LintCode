# -*- coding: utf-8 -*-
"""
@title: 数组中数字出现次数
@author: evestone
"""


# 数组中只出现一次的两个数字
def twiceAppear(arr):
    res = arr[0]
    for item in arr[1:]:
        res = res ^ item
    index = 0
    # 查找第几位为1
    while res & 1 == 0:
        res = res >> 1
        index += 1
    num1, num2 = "#", "#"
    for item in arr:
        if (item >> index) & 1 == 0:
            if num1 == "#":
                num1 = item
            else:
                num1 = num1 ^ item
        else:
            if num2 == "#":
                num2 = item
            else:
                num2 = num2 ^ item
    return num1, num2


# 数组中唯一只出现一次的数字（其他数字出现三次）
def onceApear(arr):
    bit_arr = [0]*32
    # 统计二进制中每一位为1的总数
    for item in arr:
        bitMask = 1
        for i in range(32):
            bit = item & bitMask
            if bit != 0:
                bit_arr[i] += 1
            bitMask = bitMask << 1
    result = 0
    # 所有位取余3不为0的数量
    for i in range(31, -1, -1):
        result = result << 1
        result += bit_arr[i]%3
    return result


if __name__ == '__main__':
    arr = [1, 4, 1, 2, 5, 2, 5, 6]
    print(twiceAppear(arr))

    arr = [1, 1, 1, 3, 3, 3, 4, 12, 12, 12]
    print(onceApear(arr))
