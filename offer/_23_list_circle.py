# -*- coding: utf-8 -*-
"""
@title: 查找链表的环
@author: evestone
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 查找环
def has_cycle(head):
    if head is None:
        return False
    fast = low = head
    while True:
        if fast.next is not None:
            fast = fast.next.next
            low = low.next
            if fast is None or low is None:
                return False
            elif fast == low:
                return True
        else:
            return False


# 查找环入口
def detectycle(head):
    if head is None:
        return None
    fast = low = head
    while True:
        if fast.next is not None:
            fast = fast.next.next
            low = low.next
            if fast is None or low is None:
                return None
            elif fast == low:
                break
        else:
            return None
    p1, p2 = head, fast
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


if __name__ == '__main__':
    for i in range(10):
        locals()['node' + str(i)] = ListNode(i)

    for i in range(9):
        locals()['node' + str(i)].next = locals()['node' + str(i+1)]
    locals()['node' + str(9)].next = locals()['node' + str(5)]
    print(has_cycle(locals()['node' + str(0)]))