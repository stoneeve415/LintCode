# -*- coding: utf-8 -*-
"""
@title: 合并两个有序链表
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


def mergelist(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val < list2.val:
        head = list1
        head.next = mergelist(list1.next, list2)
    else:
        head = list2
        head.next = mergelist(list1, list2.next)
    return head


def mergelist2(list1, list2):
    head = ListNode(0)
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    if list1.val < list2.val:
        head.next = list1
        list1 = list1.next
    else:
        head.next = list2
        list2 = list2.next
    cur = head.next
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return head.next


if __name__ == '__main__':
    list1 = ListNode(2)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)
    list1.next.next.next = ListNode(7)

    list2 = ListNode(1)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)
    list2.next.next.next = ListNode(8)
    res = mergelist2(list1, list2)
    myPrint(res)