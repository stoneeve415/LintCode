# -*- coding: utf-8 -*-
"""
@title: 圆圈中最后剩下的数字
@author: evestone
"""


class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None


def lastRemain(root, n):
    while True:
        for _ in range(n-1):
            root = root.next
        root.next = root.next.next
        if root.next == root:
            return root.value


if __name__ == '__main__':
    list1 = ListNode(0)
    list2 = ListNode(1)
    list3 = ListNode(2)
    list4 = ListNode(3)
    list5 = ListNode(4)
    for i in range(1, 5):
        locals()['list'+str(i)].next = locals()['list'+str(i+1)]
    list5.next = list1
    n = 2
    print(lastRemain(list1, n))