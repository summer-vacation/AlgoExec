# -*- coding: utf-8 -*-
"""
File Name:    __init__.py.py
Author :      jynnezhang
Date:         2020/12/1 9:51 上午
Description:
"""

list1={1,2,3,5}
list2={1,2,3,4}
print(list1.issubset(list2))

class A:
    def __init__(self):
        self.a = 1
        self.b = 2
c = A()

dict1 = {"ab": 1}
if not getattr(c, 'ab', None):
    print(1)
