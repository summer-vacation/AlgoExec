# -*- coding: utf-8 -*-
"""
File Name:    coroutine.py
Author :      jynnezhang
Date:         2020/4/27 5:01 下午
Description:  协程相关学习
"""

# ----------------------------------------------------------------------


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        re = c.send(n)
        print('[PRODUCER] Consumer return: %s' % re)
    c.close()


c = consumer()
produce(c)

# ----------------------------------------------------------------------


import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
print("test")

# ----------------------------------------------------------------------

import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop2 = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop2.run_until_complete(asyncio.wait(tasks))
loop2.close()
