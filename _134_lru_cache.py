"""
@title: 134, LRU缓存策略
@author: evestone
"""


class NodeList:
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.lru = {}
        self.maxsize = capacity
        self.current_size = 0
        # list to maintain lru(head is to be removed)
        self.head = NodeList()
        self.cur_node = self.head

    """
    @param: key, value
    @return: nothing
    """
    def move_tail(self, node):
        tmp = node
        # not at tail
        if tmp.right is not None:
            tmp.left.right = tmp.right
            tmp.right.left = tmp.left
            tmp.right = None
            tmp.left = self.cur_node
            self.cur_node.right = tmp
            self.cur_node = self.cur_node.right


    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.lru:
            self.move_tail(self.lru[key])
            return self.lru[key].value
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.lru:
            self.lru[key].value = value
            self.move_tail(self.lru[key])
        else:
            if self.current_size < self.maxsize:
                new_node = NodeList(key, value)
                self.current_size += 1
                self.lru[key] = new_node

                self.cur_node.right = self.lru[key]
                self.lru[key].left = self.cur_node
                self.cur_node = self.cur_node.right
            else:
                self.lru[key] = self.lru[self.head.right.key]
                del self.lru[self.head.right.key]
                self.lru[key].key = key
                self.lru[key].value = value
                # not at tail
                if self.lru[key].right is not None:
                    self.move_tail(self.lru[key])


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    lru.set(4, 4)
    print(lru.get(4))
    print(lru.get(3))
    print(lru.get(2))
    print(lru.get(1))
    lru.set(5, 5)
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(3))
    print(lru.get(4))
    print(lru.get(5))

    # lru = LRUCache(1)
    # lru.set(2, 1)
    # lru.get(2)
    # lru.set(3, 2)
    # lru.get(2)
    # lru.get(3)
