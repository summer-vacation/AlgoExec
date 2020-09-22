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
        self.used = []

    def get(self, key: int) -> int:
        if len(self.cache) == 0:
            return -1
        if key in self.cache.keys():
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
            self.cache[key] = value
        else:
            del_key = self.used[0]
            self.cache.pop(del_key)
            self.cache[key] = value
            self.used.remove(del_key)
            self.used.append(key)


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


# >> > students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# >> > sorted(students, key=lambda s: s[2])  # 按年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#
# >> > sorted(students, key=lambda s: s[2], reverse=True)  # 按降序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
