# -*- coding: utf-8 -*-
"""

   File Name：     test_error_stack
   Author :       jing
   Date：          2020/4/10
"""


def fun1(x):
    return fun2(x)


def fun2(x):
    return x/0


if __name__ == '__main__':
    fun1(10)
