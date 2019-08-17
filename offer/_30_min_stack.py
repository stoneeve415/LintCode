# -*- coding: utf-8 -*-
"""
@title: 包含最小值的栈
@author: evestone
"""


class mStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        if not self.stack1 or val < self.stack2[-1]:
            self.stack1.append(val)
            self.stack2.append(val)
        else:
            self.stack1.append(val)

    def pop(self):
        if self.stack1[-1] == self.stack2[-1]:
            self.stack2.pop(-1)
        return self.stack1.pop(-1)

    def getMin(self):
        return self.stack2[-1]


if __name__ == '__main__':
    mstack = mStack()
    mstack.push(3)
    mstack.push(4)
    mstack.push(2)
    mstack.push(1)
    print(mstack.getMin())
    print(mstack.pop())
    print(mstack.getMin())
    print(mstack.pop())
    print(mstack.getMin())
    mstack.push(0)