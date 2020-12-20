# -*- coding: utf-8 -*-
"""
File Name:    singlepart.py
Author :      jynnezhang
Date:         2020/12/18 11:27 下午
Description:

单例模式
"""
import threading
import time


class test:
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def test2(self):
        fd = open('UlBDOe.py')
        # read 返回所有
        # readline 返回第一行
        # readlines 列表返回所有行
        for line in fd.readline():
            print(line)


def tets3(s):
    f = open('out.txt', "w")
    i = 10
    while i > 0:
        f.write(threading.current_thread().getName() + ": " + s + '\n')
        print(threading.current_thread().getName() + '\n')
        time.sleep(1)
        i -= 1


t1 = threading.Thread(target=tets3, args=('111', ))
t2 = threading.Thread(target=tets3, args=('222', ))

t1.start()
t2.start()
t1.join()
t2.join()

a = test()
b = test()
a.test2()
print(id(a))
print(id(b))
