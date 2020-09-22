# -*- coding: utf-8 -*-
"""

   File Name：     product_except_self
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/907/
   除自身以外数组的乘积
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

    # 从后往前遍历一遍，用结果数组来存储除当前数外的后面所有数的乘积
    # 从前往后遍历，用nums存储除当前数外前面的所有数乘积，再把与结果数组乘积相乘得到除当前数以外所有数的乘积
    def productExceptSelf3(self, nums):
        n = len(nums)
        res = [1] * n
        for i in range(n-2, -1, -1):
            res[i] = nums[i + 1] * res[i + 1]
        for i in range(1, n):
            res[i] *= nums[i - 1]
            nums[i] *= nums[i - 1]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf3([4, 5, 3, 2, 1]))

