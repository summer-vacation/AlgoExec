# -*- coding: utf-8 -*-
"""

   File Name：     intersect
   Author :       jing
   Date：          2019-12-08
"""


class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                d = nums2.index(i)
                nums2.pop(d)
                if len(nums2) == 0:
                    break
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    print(Solution().intersect(nums1, nums2))
