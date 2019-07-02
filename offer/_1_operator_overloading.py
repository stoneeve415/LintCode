# -*- coding: utf-8 -*-
"""
@title: 操作符重载
@author: evestone
"""

'''
__init__       构造函数       X=Class()
__del__        析构函数       对象销毁
__add__        +              X+Y,X+=Y
__or__         |              X|Y,X|=Y
__repr__       打印转换       print X，repr(X)
__str__        打印转换       print X，str(X)
__call__       调用函数       X()
__getattr_     限制           X.undefine
__setattr__    取值           X.any=value
__getitem__    索引           X[key]，                         
__len__        长度           len(X)
__cmp__        比较           X==Y,X<Y
__lt__         小于           X<Y
__eq__         等于           X=Y
__radd__       Right-Side +   +X
__iadd__       +=             X+=Y
__iter__       迭代           For In 
'''


class MyTime:
    def __init__(self, m, d):
        self.month = m
        self.day = d

    # 重载 ‘+’
    def __add__(self, other):
        print('overloading +')
        return self.__class__(self.month + other.month, self.day + other.day)

    # 重载 ‘+=’
    def __iadd__(self, other):
        print('overloading +=')
        self.month += other.month
        self.day += other.day
        return self


if __name__ == '__main__':
    t1 = MyTime(1, 2)
    t2 = MyTime(1, 3)
    try:
        t = t1 + t2
        print(t.month, t.day)
        t += t1
        print(t.month, t.day)
    except ArithmeticError:
        print('error occur')

