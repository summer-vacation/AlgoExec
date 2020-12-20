# -*- coding: utf-8 -*-
"""
File Name:    lemonade-change.py
Author :      jynnezhang
Date:         2020/12/10 4:47 下午
Description:
https://leetcode-cn.com/problems/lemonade-change/
"""


class Solution:
    def lemonadeChange(self, bills=[]) -> bool:
        if not bills:
            return True
        changes = {5: 0, 10: 0}
        for bill in bills:
            need_changed = bill - 5
            if not need_changed:
                changes[5] += 1
            else:
                if need_changed == 5:
                    if changes[5] >= 1:
                        changes[5] -= 1
                        changes[10] += 1
                    else:
                        return False
                elif need_changed == 15:
                    if changes[10] >= 1 and changes[5] >= 1:
                        changes[10] -= 1
                        changes[5] -= 1
                    elif changes[5] >= 3:
                        changes[5] -= 3
                    else:
                        return False
        return True


if __name__ == '__main__':
    print(Solution().lemonadeChange([5,5,5,10]))
