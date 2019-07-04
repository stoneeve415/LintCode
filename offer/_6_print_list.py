# -*- coding: utf-8 -*-
"""
@title: 从尾到头打印链表
@author: evestone
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reversePrint(root):
    if root.next:
        reversePrint(root.next)
    print(root.val)


if __name__ == '__main__':
    for i in range(10):
        locals()['node' + str(i)] = ListNode(i)

    for i in range(9):
        locals()['node' + str(i)].next = locals()['node' + str(i+1)]
    reversePrint(locals()['node' + str(0)])