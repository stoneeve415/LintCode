# -*- coding: utf-8 -*-
"""
@title: 复杂链表复制
@author: evestone
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.sibling = None


# O(n2)复杂度
def cloneList1(head):
    if head is None:
        return None
    tmp = head
    root = Node(head.value)
    cur = root
    # 复制主链表
    while tmp.next:
        node = Node(tmp.next.value)
        cur.next = node
        cur = cur.next
        tmp = tmp.next
    tmp = head
    cur = root
    while tmp:
        if tmp.sibling:
            num = tmp.sibling.value
            p = root
            # 从头查找兄弟节点位置
            while p.value != num:
                p = p.next
            cur.sibling = p
            cur = cur.next
            tmp = tmp.next
        else:
            tmp = tmp.next
    return root


# O(n)复杂度 使用hashmap实现旧节点到新节点映射
def cloneList2(head):
    if head is None:
        return None
    tmp = head
    root = Node(head.value)
    cur = root
    hash = {}
    hash[id(tmp)] = cur
    # 复制主链表
    while tmp.next:
        node = Node(tmp.next.value)
        cur.next = node
        cur = cur.next
        tmp = tmp.next
        hash[id(tmp)] = cur
    tmp = head
    cur = root
    while tmp:
        if tmp.sibling:
            # 通过hashMap找到节点所在位置
            cur.sibling = hash[id(tmp.sibling)]
            cur = cur.next
            tmp = tmp.next
        else:
            tmp = tmp.next
    return root


# O(n)复杂度
def cloneList3(head):
    if head is None:
        return None
    tmp = head
    while tmp:
        node = Node(tmp.value)
        node.next = tmp.next
        tmp.next = node
        tmp = tmp.next.next
    tmp = head
    while tmp:
        if tmp.sibling:
            tmp.next.sibling = tmp.sibling.next
        tmp = tmp.next.next
    new_head = head.next
    tmp = new_head
    while tmp.next:
        tmp.next = tmp.next.next
        tmp = tmp.next
    return new_head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.sibling = Node(3)

    cur2 = head.next
    cur2.next = head.sibling
    cur2.sibling = Node(5)

    cur3 = cur2.next
    cur3.next = Node(4)

    cur4 = cur3.next
    cur4.sibling = cur2
    cur4.next = cur2.sibling

    # res1 = cloneList1(head)
    # res2 = cloneList2(head)
    res3 = cloneList3(head)

    a = 1
