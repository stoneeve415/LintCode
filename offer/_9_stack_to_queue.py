# -*- coding: utf-8 -*-
"""
@title: 两个栈模拟队列
@author: evestone
"""


class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if not self.stack2:
            if not self.stack1:
                raise ('error')
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if not self.stack2:
            if not self.stack1:
                raise ('error')
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
        return self.stack2[-1]