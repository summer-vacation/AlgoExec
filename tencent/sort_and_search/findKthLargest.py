# -*- coding: utf-8 -*-
"""

   File Name：     findKthLargest
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/928/
    数组中的第K个最大元素
"""


class Solution:
    def findKthLargest(self, nums, k: int):
        if k == 1 and len(nums) == 1:
            return nums[k]
        nums.sort(reverse=True)
        return nums[k-1]

    # 最大的k个数
    def findKSmallest(self, nums, k: int) -> int:
        n = len(nums)
        if k <= 0 or k > n:
            return list()
        start = 0
        end = n - 1
        mid = self.partition(nums, start, end)
        while k - 1 != mid:
            if k - 1 > mid:
                start = mid + 1
                mid = self.partition(nums, start, end)
            elif k - 1 < mid:
                end = mid - 1
                mid = self.partition(nums, start, end)
        res = nums[:mid + 1]
        # res.sort()
        return res

    def partition(self, numbers, low, high):
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] <= key:
            # while low < high and numbers[high] >= key:        # 最小的K个数
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] >= key:
            # while low < high and numbers[low] >= key:          # 最小的K个数
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        return low


if __name__ == '__main__':
    print(Solution().findKSmallest([3,2,3,1,2,4,5,5,6], 4))
