# -*- coding: utf-8 -*-
"""

   File Name：     reversePairs
   Author :       jing
   Date：          2020/4/24

https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

逆序对
"""


class Solution:
    def reversePairs(self, nums) -> int:
        """
        小到大排序，每次取最小的，那么它在原list中的位置就代表的它前面有多少个比他大的
        然后删除掉当前最小，取下一个最小

        超时了
        :param nums:
        :return:
        """
        if nums is None or len(nums) < 2:
            return 0
        sorted_nums = sorted(nums)
        count = 0
        for num in sorted_nums:
            index = nums.index(num)
            count += index
            nums.remove(num)
        return count

    def reversePairs2(self, nums) -> int:
        """
        归并 排序
        :param nums:
        :return:
        """
        global cnt
        cnt = 0
        self.guibing(nums)
        return cnt % 1000000007

    def guibing(self, data):
        global cnt
        if len(data) == 1:
            return data
        mid = len(data) // 2
        left = self.guibing(data[:mid])
        right = self.guibing(data[mid:])
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                cnt += len(left) - i  # 计算逆序对的数量
                j += 1
        res += left[i:]
        res += right[j:]
        return res


print(Solution().reversePairs2([1, 3, 2, 3, 1]))
