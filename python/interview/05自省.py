# -*- coding: utf-8 -*-
"""
File Name:    05自省.py
Author :      jynnezhang
Date:         2020/12/1 11:32 上午
Description:
"""

a = [1, 2, 3]
b = {'a': 1, 'b': 2, 'c': 3}
c = True
print(type(a), type(b), type(c))  # <type 'list'> <type 'dict'> <type 'bool'>
print(isinstance(a, list))  # True
print(dir(a))           # 获取所有的方法
if hasattr(b, 'a'):
    print(True)


class A:
    def __init__(self):
        self.a = 1


if hasattr(A, 'a'):
    print(True)

