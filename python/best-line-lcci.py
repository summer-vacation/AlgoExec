# -*- coding: utf-8 -*-
"""
File Name:    best-line-lcci.py
Author :      jynnezhang
Date:         2020/11/12 11:45 下午
Description:
https://leetcode-cn.com/problems/best-line-lcci/
"""


class Solution:
    def bestLine(self, points):
        ret = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] - points[j][0] == 0:
                    k = points[i][0]
                    b = 0
                elif points[i][1] == points[j][1]:
                    k = 0
                    b = points[i][1]
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = points[i][1] - (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])*points[i][0]
                key = str(k) + '-' + str(b)
                if key not in ret.keys():
                    ret[key] = []
                if i not in ret[key]:
                    ret[key].append(i)
                if j not in ret[key]:
                    ret[key].append(j)
        max_num, max_num_k = 0, 0
        for key, value in ret.items():
            value.sort()
            if len(value) > max_num:
                max_num = len(value)
                max_num_k = key
            if len(value) == max_num:
                if value[0] < ret[max_num_k][0]:
                    max_num = len(value)
                    max_num_k = key
                elif value[0] == ret[max_num_k][0] and value[1] < ret[max_num_k][1]:
                    max_num = len(value)
                    max_num_k = key
        return [ret[max_num_k][0], ret[max_num_k][1]]


if __name__ == '__main__':
    print(Solution().bestLine(
        [[-20398, -20631], [3544, -25103], [-12602, -17934], [-21077, -20589], [-42421, -34121], [-13836, -57776],
         [-23894, -15740], [-35969, 44416], [20924, 7570], [8073, -21024], [-13406, -30413], [-48433, -11240],
         [6794, -16545], [-8554, 37203], [4236, -7587], [-28748, -10765]]))
