# -*- coding: utf-8 -*-
"""
@title: 两个单向链表的公共节点
@author: evestone
"""


class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

def commonNode(list1, list2):
    l1, l2 = 0, 0
    tmp = list1
    # 计算两个链表长度
    while tmp:
        l1 += 1
        tmp = tmp.next
    tmp = list2
    while tmp:
        l2 += 1
        tmp = tmp.next
    # 长链表先走多余的长度
    if l1 < l2:
        tmp = l2 - l1
        while tmp:
            list2 = list2.next
            tmp += 1
    else:
        tmp = l2 - l1
        while tmp:
            list1 = list1.next
            tmp += 1
    while list1 and list2:
        if list1.value == list2.value:
            return list1.value
        list1 = list1.next
        list2 = list2.next
    return None




if __name__ == '__main__':
    pass


