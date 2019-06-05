# -*- coding: utf-8 -*-
"""
@title: 24. LFU缓存
@author: evestone
"""

'''
思路一：使用双向链表
'''


# 方法一
# 新插入元素时，插入到头部，然后根据访问次数向后移
# 访问数据时，更新当前元素的访问次数，然后根据访问次数向后移
class NodeList1_1:
    def __init__(self, key=None, value=None, nums=0):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.nums = nums


class LFUCache1_1:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.maxsize = capacity
        self.head = NodeList1_1()
        self.lfu = {}

    """
    @descrip: move the node from left to right according to nums
    @param: node: NodeList
    @return: nothing
    """

    def update(self, node):
        # write your code here
        p = node
        while p.right is not None and node.nums >= p.right.nums:
            p = p.right
        if p == node or node.right is None:
            return
        else:
            node.left.right = node.right
            node.right.left = node.left
            if p.right is None:
                p.right = node
                node.left = p
                node.right = None
            else:
                node.right = p.right
                p.right.left = node
                p.right = node
                node.left = p

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.lfu:
            self.lfu[key].value = value
            self.lfu[key].nums += 1
            self.update(self.lfu[key])
        else:
            if len(self.lfu) < self.maxsize:
                self.lfu[key] = NodeList1_1(key, value)
                # the first node
                if self.head.right is None:
                    self.head.right = self.lfu[key]
                    self.lfu[key].left = self.head
                else:
                    self.head.right.left = self.lfu[key]
                    self.lfu[key].right = self.head.right
                    self.head.right = self.lfu[key]
                    self.lfu[key].left = self.head
                    self.update(self.lfu[key])
            else:
                key_remove = self.head.right.key
                self.lfu[key] = self.lfu[key_remove]
                del self.lfu[key_remove]
                # update node properties
                self.lfu[key].key = key
                self.lfu[key].value = value
                self.lfu[key].nums = 0
                self.update(self.lfu[key])

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.lfu:
            self.lfu[key].nums += 1
            self.update(self.lfu[key])
            return self.lfu[key].value
        else:
            return -1

    def test(self):
        self.set(2, 2)
        self.set(1, 1)
        print(self.get(2))
        print(self.get(1))
        print(self.get(2))
        self.set(3, 3)
        self.set(4, 4)
        print(self.get(3))
        print(self.get(2))
        print(self.get(1))
        print(self.get(4))


# 方法二（较方法一快）
# 新插入元素时，插入到尾部，然后根据访问次数向前移
# 访问数据时，更新当前元素的访问次数，然后根据访问次数向后移
class NodeList1_2:
    def __init__(self, key=None, value=None, nums=0):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.nums = nums


class LFUCache1_2:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.maxsize = capacity
        self.head = NodeList1_2()
        self.tail = self.head
        self.lfu = {}

    """
    @descrip: move the node from left to right according to nums
    @param: node: NodeList
    @return: nothing
    """
    def update_left(self, node):
        # write your code here
        p = node
        while node.nums <= p.left.nums:
            p = p.left
            if node.nums == p.nums:
                break
        if p.right == node or node.left == self.head:
            return
        else:
            node.left.right = None
            self.tail = node.left
            node.left = p
            node.right = p.right
            p.right.left = node
            p.right = node

    """
       @descrip: move the node from right to left according to nums
       @param: node: NodeList
       @return: nothing
    """
    def update_right(self, node):
        # write your code here
        p = node
        while p.right is not None and node.nums >= p.right.nums:
            p = p.right
        if p == node or node.right is None:
            return
        else:
            node.left.right = node.right
            node.right.left = node.left
            if p.right is None:
                p.right = node
                node.left = p
                node.right = None
                self.tail = node
            else:
                node.right = p.right
                p.right.left = node
                p.right = node
                node.left = p

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.lfu:
            self.lfu[key].value = value
            self.lfu[key].nums += 1
            self.update_right(self.lfu[key])
        else:
            if len(self.lfu) < self.maxsize:
                self.lfu[key] = NodeList1_2(key, value)
                # the first node
                self.tail.right = self.lfu[key]
                self.lfu[key].left = self.tail
                self.tail = self.tail.right
                self.update_left(self.lfu[key])
            else:
                key_remove = self.head.right.key
                self.lfu[key] = self.lfu[key_remove]
                del self.lfu[key_remove]
                # update node properties
                self.lfu[key].key = key
                self.lfu[key].value = value
                self.lfu[key].nums = 0
                self.update_right(self.lfu[key])

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.lfu:
            self.lfu[key].nums += 1
            self.update_right(self.lfu[key])
            return self.lfu[key].value
        else:
            return -1

    def test(self):
        self.set(2, 2)
        self.set(1, 1)
        print(self.get(2))
        print(self.get(1))
        print(self.get(2))
        self.set(3, 3)
        self.set(4, 4)
        print(self.get(3))
        print(self.get(2))
        print(self.get(1))
        print(self.get(4))


'''
思路二：使用二维字典，第一维是访问的次数，第二维是key（第二位是一个有序字典）
'''


from collections import defaultdict, OrderedDict


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.maxsize = capacity
        # key:(frequence,value)
        self.lfu = {}
        # the first axis is frequence, and the second axis is a order dict(same freq)
        # frequence:key:@
        self.strategy = defaultdict(OrderedDict)
        # least frequence
        self.least = 1

    """
    @descrip: update key
    @param: key
    @return: nothing
    """

    def update(self, key):
        # write your code here
        freq, value = self.lfu[key]
        self.strategy[freq].pop(key)
        self.strategy[freq+1][key] = '@'
        self.lfu[key] = (freq+1, value)
        # curent freq has no element
        if len(self.strategy[self.least]) == 0:
            self.least += 1


    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.lfu:
            freq = self.lfu[key][0]
            self.lfu[key] = (freq, value)
            self.update(key)
        else:
            if len(self.lfu) >= self.maxsize:
                remove_key, _ = self.strategy[self.least].popitem(last=False)
                self.lfu.pop(remove_key)
            self.lfu[key] = (1, value)
            self.strategy[1][key] = '@'
            # set least to 1 after insert a new element
            self.least = 1



    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.lfu:
            freq, value = self.lfu[key]
            self.update(key)
            return value
        else:
            return -1

    def test(self):
        self.set(2, 2)
        self.set(1, 1)
        print(self.get(2))
        print(self.get(1))
        print(self.get(2))
        self.set(3, 3)
        self.set(4, 4)
        print(self.get(3))
        print(self.get(2))
        print(self.get(1))
        print(self.get(4))


if __name__ == '__main__':
    lfu = LFUCache(3)
    lfu.test()
