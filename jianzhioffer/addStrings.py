# -*- coding: utf-8 -*-
"""
File Name:    addStrings.py
Author :      jynnezhang
Date:         2020/5/26 6:58 下午
Description:
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1, num2 = num1[::-1], num2[::-1]
        for i, digit in enumerate(num2):
            num1[i] += num2[i]

        num1 = self.CarrySolver(num1)
        num1 = num1[::-1]
        return "".join(str(x) for x in num1)

    def CarrySolver(self, nums):
        # 这个函数的功能是：将输入的数组中的每一位处理好进位
        # 举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
        i = 0
        while i < len(nums):
            if nums[i] >= 10:
                carrier = nums[i] // 10
                if i == len(nums) - 1:
                    nums.append(carrier)
                else:
                    nums[i + 1] += carrier
                nums[i] %= 10
            i += 1

        return nums


if __name__ == '__main__':
    print(Solution().addStrings("123", "496"))


