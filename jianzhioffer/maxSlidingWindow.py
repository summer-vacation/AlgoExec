# -*- coding: utf-8 -*-
"""
File Name:    maxSlidingWindow.py
Author :      jynnezhang
Date:         2020/4/30 10:48 上午
Description:

滑动窗口的最大值
https://leetcode-cn.com/problems/sliding-window-maximum/
https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
"""


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if nums is None or len(nums) == 0 or k == 0:
            return []
        res = []
        lens = len(nums)
        if k > lens:
            return self.getMax(nums)
        else:
            start = 0
            end = k
            while end <= lens:
                res.append(self.getMax(nums[start:end]))
                start = start + 1
                end = end + 1
            return res

    def getMax(self, window):
        window.sort(reverse=True)
        return window[0]

    def maxSlidingWindow2(self, nums, k: int):
        deque = []
        result = []     # deque也可以用collection里的双端队列实现
        for i in range(0, len(nums)):
            while deque and nums[i] > nums[deque[-1]]:    # 只存有可能成为最大值的数字的index进deque
                deque.pop()
            deque.append(i)
            while i-deque[0] > k-1:   # 如果相距超过窗口k长度则弃掉
                deque.pop(0)
            if i >= k-1:
                result.append(nums[deque[0]])   # 这过程中始终保持deque[0]为最大值的index
        return result

    def maxSlidingWindow3(self, nums, k: int):
        import collections
        if not nums or k == 0:
            return []
        deque = collections.deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]:     # 删掉超出长度的
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


print(Solution().maxSlidingWindow3(nums= [1,3,-1,-3,5,3,6,7], k = 3))
