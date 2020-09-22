# -*- coding: utf-8 -*-
"""

   File Name：     permutation_str
   Author :       jing
   Date：          2020/3/23

   字符串中所有字符的排列
"""

import itertools


class Solution:
    # python 内置实现了排列方法
    def Permutation(self, ss):
        res = set(itertools.permutations(ss))
        return sorted(list(map(lambda x: ''.join(x), res)))

    # 固定第一个字符，
    def Permutation2(self, ss):
        # write code here
        out = set()
        if len(ss) == 0:
            return out
        charlist = list(ss)
        self.permutation(charlist, 0, out)
        return sorted(list(out))

    def permutation(self, ss, begin, out):
        if begin == len(ss) - 1:
            out.add(''.join(ss[:]))
        else:
            for i in range(begin, len(ss)):
                # 如果是重复字符，跳过
                if ss[begin] == ss[i] and begin != i:
                    continue
                else:
                    # 依次与后面每个字符交换
                    ss[begin], ss[i] = ss[i], ss[begin]
                    self.permutation(ss, begin + 1, out)
                    # 回到上一个状态
                    ss[begin], ss[i] = ss[i], ss[begin]


if __name__ == '__main__':
    print(Solution().Permutation2("abc"))
