# -*- coding: utf-8 -*-
"""
File Name:    16单例模式.py
Author :      jynnezhang
Date:         2020/12/1 12:39 下午
Description:
"""

print("1、使用__new__方法")


# 1、使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1


print("--------------")
print("2 共享属性")


# 2 共享属性
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


print("--------------")
print("3 装饰器")


# 3 装饰器
def singleton(cls):
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class MyClass3:
    a = 1

    def __init__(self, x=0):
        self.x = x


m1 = MyClass3(1)
m2 = MyClass3(2)
print(m1.x, m2.x)   # 1, 1


print("--------------")
print("4 模块")


# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
# 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass


my_singleton = My_Singleton()

# to use
# from mysingleton import my_singleton
my_singleton.foo()
