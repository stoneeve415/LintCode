"""
@title: 88, 二叉树最近公共祖先
@author: evestone
"""

'''
存在父指针
'''


def lowestCommonAncestorII(root, A, B):
    # write your code here
    _dict = {}
    while A != None:
        _dict[A]=True
        A = A.parent
    while B != None:
        if B in _dict:
            return B
        B = B.parent
    return None


# 转换为链表求交点
def Hight(root, node):
    length = 0
    while node != None:
        length += 1
        node = node.parent
    return length


def lowestCommonAncestor1(root, p, q):
    if root == None or p == None or q ==None:
        return None
    len1 = Hight(root, p)
    len2 = Hight(root, q)
    while len1 > len2:
        p = p.parent
        len1 -= 1
    while len2 > len1:
        q = q.parent
        len2 -= 1
    while p and q and p!=q:
        p = p.parent
        q = q.parent
    if p == q:
        return p
    else:
        return None


'''
二叉搜索树
'''


def lowestCommonAncestor2(root, p, q):
    if p.val < q.val:          #p大，q小
        p, q = q, p
    while root:
        # if root == p or root == q:
        #     return root
        # if root.val < p.val and root.val > q.val:
        #     return root
        if root.val < q.val:
            root = root.right
        if root.val > p.val:
            root = root.left
        else:      #该句else等价于上面被注释掉的四句
            return root


'''
普通二叉树
'''


# 暴力方法
def lowestCommonAncestor(root, A, B):
    # write your code here
    if root == None:
        return None
    elif root == A or root == B:
        return root
    left = lowestCommonAncestor(root.left, A, B)
    right = lowestCommonAncestor(root.right, A, B)
    if left != None and right != None:
        return root
    elif left != None:
        return left
    elif right != None:
        return right
    else:
        return None

# tarian算法
# RMQ倍增算法
# 线段树算法