# -*- coding: utf-8 -*-
"""

   File Name：     videoStitching
   Author :       jing
   Date：          2020/3/26
"""


class Solution:
    def videoStitching(self, clips, T: int) -> int:
        if clips is None or len(clips) == 0:
            return -1
        dp = [0] * T
        clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        for c in clips:
            if dp[0] == 0 and c[0] > 0:
                return -1
            if c[0] > T:
                continue

    def videoStitching2(self, clips, T: int) -> int:
        last_end, end, res = -1, 0, 0
        for i, j in sorted(clips, key=lambda x: (x[0],-x[1])):
            if end >= T or i > end:
                break
            if last_end < i <= end:
                res += 1
                last_end = end
            end = max(end, j)

        return res if end >= T else -1


if __name__ == '__main__':
    print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
