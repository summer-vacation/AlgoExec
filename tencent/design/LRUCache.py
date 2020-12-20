# -*- coding: utf-8 -*-
"""

   File Name：     LRUCache
   Author :       jing
   Date：          2020/3/21

   https://leetcode-cn.com/explore/interview/card/tencent/225/design/925/
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.key = []

    def get(self, key: int) -> int:
        # 存在就get
        if key in self.cache.keys():
            self.key.remove(key)
            self.key.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            if self.cache[key] != value:
                self.cache[key] = value
                self.key.remove(key)
                self.key.append(key)
        if key not in self.cache.keys():
            if len(self.cache) < self.capacity:
                self.cache[key] = value
                self.key.append(key)
            else:
                # 找到最近最少用的
                self.cache.pop(self.key[0])
                self.key.remove(self.key[0])
                self.cache[key] = value
                self.key.append(key)


class LRUCache2:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    # # print(cache.get(2))
    # cache.put(2, 1)
    # cache.put(2, 2)
    # print(cache.get(2))
    # cache.put(1, 1)
    # cache.put(4, 1)
    # print(cache.get(2))


# >> > students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# >> > sorted(students, key=lambda s: s[2])  # 按年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#
# >> > sorted(students, key=lambda s: s[2], reverse=True)  # 按降序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
