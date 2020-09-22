# -*- coding: utf-8 -*-
"""
File Name:    generator.py
Author :      jynnezhang
Date:         2020/4/27 5:17 下午
Description:  生成器！！
"""

# -----------------------------------------------------------------

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(3))      # 生成器
print(g)

# 访问生成器内容
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
# print(next(g))  # StopIteration


# -----------------------------------------------------------------

def odd():
    """
    每次遇到yield就会停止，，下次调用next会从上次停止的地方继续运行
    :return:
    """
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
print(next(o))
next(o)  # 不打印yield的内容
next(o)
# next(o)  # StopIteration


# -------------------------------------------------------------------

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for i in fib(6):
    print(i)


# 获取返回值
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# -------------------------------------------------------------------------------
"""
send()
"""


def MyGenerator():
    value = yield 1
    print(value)
    value = 0
    yield value


gen = MyGenerator()
print(next(gen))
print(gen.send(2))
# print(gen.send(3))        # StopIteration


# -------------------------------------------------------------------------------
"""
yield from
"""


def generator_1(titles):
    yield titles


def generator_2(titles):
    yield from titles


titles = ['Python', 'Java', 'C++']
for title in generator_1(titles):
    print('生成器1:', title)
for title in generator_2(titles):
    print('生成器2:', title)
# 输出：
# 生成器1: ['Python', 'Java', 'C++']
# 生成器2: Python
# 生成器2: Java
# 生成器2: C++


# -------------------------------------------------------------------------------
"""
yield from
"""


def generator_11():
    total = 0
    while True:
        x = yield
        print('加', x)
        if not x:
            break
        total += x
    return total


def generator_21():     # 委托生成器
    while True:
        total = yield from generator_11()    # 子生成器
        print('加和总数是:', total)


# g11 = generator_11()
# g11.send(None)
# g11.send(2)
# g11.send(3)
# g1.send(None)
g21 = generator_21()
g21.send(None)
g21.send(2)
g21.send(3)
g21.send(None)

