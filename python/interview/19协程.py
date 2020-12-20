# -*- coding: utf-8 -*-
"""
File Name:    19协程.py
Author :      jynnezhang
Date:         2020/12/1 7:41 下午
Description:
"""


def foo():
    print("starting...")
    res = 1
    while True:
        yield '4'
        res += 1
        print("res:", res)


g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))
