# -*- coding: utf-8 -*-
"""

   File Name：     StringIterator
   Author :       jing
   Date：          2020/4/2
"""


class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.a_index = 0
        self.n_count = 0
        self.num = 0

    def next(self) -> str:
        num_index = self.a_index + 1
        count = ""
        while self.compressedString[num_index].isdigit():
            count += self.compressedString[num_index]
            num_index += 1
        self.n_count = int(count)
        if self.n_count > self.num:
            self.num += 1
        else:
            self.a_index += self.n_count
            self.num = 1
        if self.index > len(self.compressedString)//2:
            return None
        return self.compressedString[self.a_index]

    def hasNext(self) -> bool:
        if self.a_index >= len(self.compressedString)//2 and self.num >= int(self.compressedString[self.index * 2-1]):
            return False
        return True


# Your StringIterator object will be instantiated and called as such:
obj = StringIterator("L1e2t1C1o1d1e1")
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
