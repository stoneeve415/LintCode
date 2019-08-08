# -*- coding: utf-8 -*-
"""
@title: 反转链表
@author: evestone
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def myPrint(root):
    while root:
        print(root.val)
        root = root.next


def reverse(root):
    cur = root
    pre = None
    while cur.next:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    cur.next = pre
    return cur


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    res = reverse(root)
    myPrint(res)

