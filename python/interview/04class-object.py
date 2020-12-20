# -*- coding: utf-8 -*-
"""
File Name:    04class-object.py
Author :      jynnezhang
Date:         2020/12/1 10:47 上午
Description:
"""


class Test(object):
    num_of_instance = 0     # 所有类、实例共享

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print(Test.num_of_instance)  # 0
    t1 = Test('jack')
    print(Test.num_of_instance)  # 1
    t2 = Test('lucy')
    print(Test.num_of_instance)
    print(t1.name, t1.num_of_instance)  # jack 2
    print(t2.name, t2.num_of_instance)  # lucy 2

