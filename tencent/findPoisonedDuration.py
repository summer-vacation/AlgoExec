# -*- coding: utf-8 -*-
"""

   File Name：     findPoisonedDuration
   Author :       jing
   Date：          2020/3/31

输入: [1,4], 2
输出: 4
原因: 在第 1 秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒钟结束。
在第 4 秒开始时，提莫再次攻击艾希，使得艾希获得另外 2 秒的中毒时间。
所以最终输出 4 秒。
"""


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries is None or len(timeSeries) == 0 or duration == 0:
            return 0
        len_t = len(timeSeries)
        if len_t == 1:
            return duration
        poisoned_duration = duration
        for i in range(len_t-1, 0, -1):
            cur = timeSeries[i]
            pre = timeSeries[i-1]
            if cur - pre >= duration:
                poisoned_duration += duration
            else:
                poisoned_duration = poisoned_duration + (cur - pre)
        return poisoned_duration
