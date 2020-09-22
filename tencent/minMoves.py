# -*- coding: utf-8 -*-
"""

   File Name：     minMoves
   Author :       jing
   Date：          2020/3/31

   使所有元素想等的最小移动步数

   每次移动可以使 n - 1 个元素增加 1     ==>     每次移动一个数，使其减1

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

等价于  [1,2,3]  =>  [1,1,3]  =>  [1,1,2]  =>  [1,1,1]
"""


class Solution:
    def minMoves(self, nums) -> int:
        if nums is None or len(nums) < 2:
            return 0
        return sum(nums)-min(nums)*len(nums)
