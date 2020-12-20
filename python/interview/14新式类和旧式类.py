# -*- coding: utf-8 -*-
"""
File Name:    14新式类和旧式类.py
Author :      jynnezhang
Date:         2020/12/1 12:25 下午
Description:

旧式类：从左到右深度优先
新式类：C3算法
"""


class D:
    def foo1(self):
        print("A")


class B(D):
    def foo2(self):
        pass


class C(D):
    def foo1(self):
        print("C")


class A(B, C):
    pass


a = A()
print(a.foo1())        # 旧式类会返回D，新式类是C

"""
    D
B       C
  |   |
    A
在经典对象模型中，方法和属性的查找链是按照从左到右，深度优先的方式进行查找。所以当A的实例b
要使用属性a时，它的查找顺序为:A->B->D->C->A，这样做就会忽略类C的定义a，而先找到的基类D的
属性a，这是一个bug，这个问题在新式类中得到修复，
新的对象模型采用的是从左到右，广度优先的方式
进行查找，所以查找顺序为A->B->C->D，可以正确的返回类C的属性a。
"""
