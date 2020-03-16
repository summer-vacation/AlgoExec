# -*- coding: utf-8 -*-
"""

   File Name：     median_of_two_sorted_arrays
   Author :       jing
   Date：          2020/3/16
   https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if nums1 is None or len(nums1) == 0 and nums2 is not None:
            lens = len(nums2)
            mod = lens % 2
            if mod == 1:
                return nums2[lens//2]
            else:
                return (nums2[lens//2-1] + nums2[lens//2])/2.0
        elif nums2 is None or len(nums2) == 0 and nums1 is not None:
            lens = len(nums1)
            mod = lens % 2
            if mod == 1:
                return nums1[lens//2]
            else:
                return (nums1[lens//2 - 1] + nums1[lens//2]) / 2
        len1 = len(nums1)
        len2 = len(nums2)
        temp = []
        n1 = 0
        n2 = 0
        for i in range(int((len1+len2)/2)+1):
            if n1 < len(nums1) and n2 < len(nums2) and nums1[n1] <= nums2[n2]:
                temp.append(nums1[n1])
                n1 += 1
            elif n1 < len(nums1) and n2 < len(nums2) and nums1[n1] > nums2[n2]:
                temp.append(nums2[n2])
                n2 += 1
            elif n1 >= len(nums1):
                temp.append(nums2[n2])
                n2 += 1
            elif n2 >= len(nums2):
                temp.append(nums1[n1])
                n1 += 1

        if (len1+len2)%2 == 1:
            return temp[(len1+len2)//2]
        else:
            return (temp[(len1+len2)//2 - 1] + temp[(len1+len2)//2])/2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [1, 2, 3]))

