# -*- coding: utf-8 -*-
"""
File Name:    queue-reconstruction-by-height.py
Author :      jynnezhang
Date:         2020/11/16 1:36 下午
Description:
https://leetcode-cn.com/problems/queue-reconstruction-by-height/
"""


class Solution:
    def reconstructQueue(self, people):
        if not people or len(people) == 0:
            return people
        people.sort(key=lambda x: (-x[0], x[1]))
        i = 0
        while i < len(people):
            if i > people[i][1]:
                people.insert(people[i][1], people[i])
                people.pop(i+1)
            i += 1
        return people


if __name__ == '__main__':
    print(Solution().reconstructQueue([[7,0], [4,2], [7,1], [5,0], [6,1], [5,2], [4,4], [3,0]]))
