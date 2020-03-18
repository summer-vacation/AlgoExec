# -*- coding: utf-8 -*-
"""

   File Name：     container_with_most_water
   Author :       jing
   Date：          2020/3/17

   https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    # 超时
    def maxArea(self, height) -> int:
        if height is None or len(height) < 2:
            return 0
        max_area = 0
        i = 0
        for h in height:
            j = 0
            for hh in height[i:]:
                if i == 0:
                    i += 1
                    continue
                min_h = min(hh, h)
                max_area = max(max_area, min_h * (j+1))
                j += 1
            i += 1
        return max_area

    def maxArea2(self, height) -> int:
        if height is None or len(height) < 2:
            return 0
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            left_v = height[left]
            right_v = height[right]
            min_h = min(left_v, right_v)
            max_area = max(max_area, min_h * (right-left))
            if left_v > right_v:
                right -= 1
            else:
                left += 1

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
