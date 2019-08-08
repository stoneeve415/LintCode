# -*- coding: utf-8 -*-
"""
@title: 删除链表的节点
@author: evestone
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def delete_node(root, val):
    while root and root.value != val:
        root = root.next
    if root:
        if root.next:
            node = root.next
            root.value = node.value
            root.next = node.next
            node.next = None
            del node
        else:
            root = None
    return 

