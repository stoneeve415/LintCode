# -*- coding: utf-8 -*-
"""
@title: 查找链表的倒数第k个节点
@author: evestone
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def findKthToTail(root, k):
    first, second = root, root
    while first and k:
        first = first.next
        k -= 1
    if k != 0:
        return None
    while first:
        first = first.next
        second = second.next
    return second


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    print(findKthToTail(root, 2).val)