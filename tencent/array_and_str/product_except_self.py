# -*- coding: utf-8 -*-
"""

   File Name：     product_except_self
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/907/
"""


class Solution:
    # 超时！
    def productExceptSelf(self, nums):
        if len(nums) == 2:
            nums.reverse()
            return nums
        result = []
        for n in nums:
            s_nums = [str(x) for x in nums]
            s_nums.remove(str(n))
            result.append(eval("*".join(s_nums)))

        return result

    def productExceptSelf2(self, nums):
        l, r = 1, 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] = l
            l *= nums[i]
        for i in range(n)[::-1]:
            res[i] *= r
            r *= nums[i]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf2([4, 5, 3, 2, 1]))

