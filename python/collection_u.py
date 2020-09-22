# -*- coding: utf-8 -*-
"""

   File Name：     collection
   Author :       jing
   Date：          2020/3/27
"""

from collections import namedtuple, Counter, defaultdict, deque, OrderedDict


Point = namedtuple('point', ['x', 'y'])
Circle = namedtuple('circle', ["x", "y", "r"])
point1 = Point(1, 1)
circle1 = Circle(0, 0, 3)
print(point1, point1.x, point1.y)       # point(x=1, y=1) 1 1
print(circle1, circle1.x, circle1.y, circle1.r)     # circle(x=0, y=0, r=3) 0 0 3

print("\n\n***************************")
od = OrderedDict([('a', 1), ('z', 2), ('c', 3)])
print(od)           # OrderedDict([('a', 1), ('z', 2), ('c', 3)])
d = dict([('a', 1), ('z', 2), ('c', 3)])
print(d)            # {'a': 1, 'z': 2, 'c': 3}

print("\n\n***************************")
c = Counter(['11', '22', '11', '33', '11', '44', '55'])
c2 = Counter("abcdefdasfdsafaf")
print(c)            # Counter({'11': 3, '22': 1, '33': 1, '44': 1, '55': 1})
print(c2)           # Counter({'a': 4, 'f': 4, 'd': 3, 's': 2, 'b': 1, 'c': 1, 'e': 1})


print("\n\n***************************")
a = defaultdict(int)
a[1] = 1
print("a['a']==", a["a"])       # a['a']== 0
