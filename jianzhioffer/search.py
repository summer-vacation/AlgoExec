# -*- coding: utf-8 -*-
"""
File Name:    search.py
Author :      jynnezhang
Date:         2020/4/30 12:53 下午
Description:

  查找指定数字的个数

  https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        left, right = 0, len(nums)-1
        while left < right and nums[left] < target:
            left += 1
        while left < right and nums[right] > target:
            right -= 1
        if left <= right:
            return right - left + 1
        else:
            return 0

    # 二分查找！！
    def search2(self, nums, target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return 0  # 没有找到, 直接返回0
        idx1 = left

        # 如果这里能够运行, 肯定是找到了target的
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # note that change to <=
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        # upper bound 应该是 right - 1
        # 返回 right - 1 - idx1 + 1
        # 退出循环时 left = right
        return left - idx1


print(Solution().search2(nums = [5,7,7,8,8,10], target = 8))
