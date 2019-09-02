# -*- coding: utf-8 -*-
"""
@title: 队列最大值
@author: evestone
"""
from collections import deque


# 滑动窗口最大值
def push(dque, num, i):
    while dque and num[dque[-1]] < num[i]:
        dque.pop()
    dque.append(i)


def maxQueue(arr, k):
    if len(arr) < k:
        return -1
    res = []
    dque = deque([])
    for i in range(k-1):
        push(dque, arr, i)

    for i in range(k-1, len(arr)):
        push(dque, arr,i)
        res.append(arr[dque[0]])
        if i - dque[0] + 1 == k:
            dque.popleft()
    return res


# 队列最大值
class mQueue:
    def __init__(self):
        self.value = []
        self.max_value = deque([])


    def push(self, num):
        if self.value is None:
            self.max_value.append(num)
        else:
            while self.max_value and self.max_value[-1] < num:
                self.max_value.pop()
            self.max_value.append(num)
        self.value.append(num)




    def pop(self,):
        if self.value is None:
            raise IndexError
        else:
            if self.value[0] == self.max_value[0]:
                self.max_value.popleft()
            self.value.pop(0)


    def max(self):
        if self.max_value:
            return self.max_value[0]
        else:
            raise IndexError


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    k = 3
    print(maxQueue(arr, k))

    mqueue = mQueue()
    mqueue.push(2)
    mqueue.push(3)
    mqueue.push(4)
    mqueue.pop()
    mqueue.pop()
    mqueue.push(5)
    print(mqueue.max())