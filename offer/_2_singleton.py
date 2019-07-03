# -*- coding: utf-8 -*-
"""
@title: 单例模式
@author: evestone
"""


# 使用元类
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Foo1(metaclass=Singleton):
    pass


# new 方法
class Foo2(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    a = Foo1()
    b = Foo1()
    print(id(a) == id(b))  # 得到 True

    a = Foo2()
    b = Foo2()
    print(id(a) == id(b))  # 得到 True
