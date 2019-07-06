# -*- coding: utf-8 -*-
"""
@title: 229 栈排序
@author: evestone
"""
import sys

# 栈排序
def stackSorting(stk):
    # write your code here
    mstack = []
    while stk:
        cur = stk.pop()
        if not mstack or cur <= mstack[-1]:
            mstack.append(cur)
        else:
            while mstack and cur > mstack[-1]:
                stk.append(mstack.pop())
            mstack.append(cur)
    while mstack:
        stk.append(mstack.pop())
    return stk

# 获取栈的最大元素
class MStack:
    def __init__(self):
        self.maxValue = -sys.maxsize
        self.mstack = []
        self.helper = []

    def push(self, x):
        if x >= self.maxValue:
            self.maxValue = x
            self.helper.append(x)
        self.mstack.append(x)

    def pop(self):
        if len(self.mstack) == 0:
            raise RuntimeError('stack is empty')
        if self.mstack[-1] == self.maxValue:
            self.helper.pop()
        self.maxValue = self.helper[-1]
        self.mstack.pop()

    def getMax(self):
        return self.maxValue


if __name__ == '__main__':
    stk = [3, 2, 1, 4, 6, 5]
    print(stackSorting(stk))
    mstack = MStack()
    mstack.push(3)
    mstack.push(2)
    mstack.push(1)
    mstack.push(4)
    mstack.push(6)
    mstack.push(5)
    print(mstack.getMax())
    mstack.pop()
    print(mstack.getMax())
    mstack.pop()
    print(mstack.getMax())
