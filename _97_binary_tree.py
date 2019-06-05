"""
@title: 97, 二叉树遍历
@author: evestone
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


'''
递归实现
'''


# 前序遍历
def pre_traverse(root):
    if root is None:
        return
    print(root.val)
    pre_traverse(root.left)
    pre_traverse(root.right)


# 中序遍历
def mid_traverse(root):
    if root is None:
        return
    mid_traverse(root.left)
    print(root.val)
    mid_traverse(root.right)


# 后序遍历
def last_traverse(root):
    if root is None:
        return
    last_traverse(root.left)
    last_traverse(root.right)
    print(root.val)


'''
非递归实现
'''


def pre_traverse_(root):
    stack = []
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            print(root.val)
            root = root.left
        if len(stack) != 0:
            root = stack.pop(-1).right


def mid_traverse_(root):
    stack = []
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            root = root.left
        if len(stack) != 0:
            root = stack.pop(-1)
            print(root.val)
            root = root.right


def last_traverse_(root):
    stack = []
    # 记录右子树是否已经访问
    pre = None
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            root = root.left
        if len(stack) != 0:
            root = stack[-1]
            if root.right is None or root.right == pre:
                print(root.val)
                pre = root
                stack.pop(-1)
                root = None
            else:
                root = root.right


'''
求树的最大深度
'''


def maxDepth(root):
    stack = []
    # 记录右子树是否已经访问
    pre = None
    max_d = 0
    cur = 0
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            root = root.left
            cur += 1
            if cur > max_d:
                max_d = cur
        if len(stack) != 0:
            root = stack[-1]
            if root.right is None or root.right == pre:
                cur -= 1
                pre = root
                stack.pop(-1)
                root = None
            else:
                root = root.right
    return max_d


'''
二叉树序列化
'''


def serialize(root):
    # write your code here
    queue = []
    res = []
    if root is None:
        return res
    queue.append(root)
    while len(queue) != 0:
        cur = queue.pop(0)
        res.append(str(cur.val))
        if cur.val != '#':
            if cur.left is not None:
                queue.append(cur.left)
            else:
                queue.append(TreeNode('#'))
            if cur.right is not None:
                queue.append(cur.right)
            else:
                queue.append(TreeNode('#'))
    return ''.join(res)


def deserialize(data):
    # write your code here
    data = data.split()
    len_ = len(data)
    if len_ == 0:
        return None
    root = TreeNode(data[0])
    queue = []
    queue.append(root)
    i = 0
    while len(queue) != 0:
        cur = queue.pop(0)
        if data[i + 1] != '#':
            cur.left = TreeNode(data[i + 1])
            queue.append(cur.left)
        if data[i + 2] != '#':
            cur.right = TreeNode(data[i + 2])
            queue.append(cur.right)
        i += 2

    return root


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    for i in range(1, 9):
        temp = 'node' + str(i)
        locals()[temp] = TreeNode(i)
    root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node6.left = node8
    mid_traverse(root)