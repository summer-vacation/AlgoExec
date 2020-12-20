# -*- coding: utf-8 -*-
"""
File Name:    内存管理.py
Author :      jynnezhang
Date:         2020/12/14 2:05 下午
Description:
"""
import sys


a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))
a.append(3)
print("a", a, id(a))
print("b", b, id(b))

c = '''12345678912'''
d = '''12345678912'''
print(id(c))
print(id(d))
c += 'a'
print("c", c, id(c))
print("d", d, id(d))

l = [4, 5, 6]
