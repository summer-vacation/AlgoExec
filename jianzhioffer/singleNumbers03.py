# -*- coding: utf-8 -*-
"""

   File Name：     singleNumbers03
   Author :       jing
   Date：          2020/4/13

   数组中数字出现的次数
   除两个数字之外，其他数字都出现了两次

   要求时间复杂度是O(n)，空间复杂度是O(1)
"""


class Solution:
    def singleNumbers(self, nums):
        if nums is None or len(nums) == 0:
            return []
        mapper = {}

        for n in nums:
            if n in mapper.keys():
                mapper[n] += 1
            else:
                mapper[n] = 1
        result = []
        for key, value in mapper.items():
            if value == 1:
                result.append(key)
        return result

    def singleNumbers2(self, nums):
        temp = 0
        for i in nums:  # 得到用于区分的数字
            temp ^= i
        num = 1
        while not (num & temp):  # 找到用于区分的数字中从右到左的第一位为1的值
            num = num << 1
        result1 = 0
        result2 = 0
        for i in nums:
            if num & i:  # 划分两个数组
                result1 ^= i  # 两个数组分别取异或
            else:
                result2 ^= i
        return [result1, result2]


print(Solution().singleNumbers2([4,1,4,3]))
