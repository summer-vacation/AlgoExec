# -*- coding: utf-8 -*-
"""

   File Name：     trap
   Author :       jing
   Date：          2020/4/4

   接雨水
"""


class Solution:
    def trap(self, height) -> int:
        if height is None or len(height) < 3:
            return 0
        n = len(height)
        # 双指针
        i, j = 0, n - 1
        result = 0
        left_max, right_max = 0, 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max < right_max:
                result += left_max - height[i]
                i += 1
            else:
                result += right_max - height[j]
                j -= 1
        return result


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
