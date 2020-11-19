# -*- coding: utf-8 -*-
"""
File Name:    master-mind-lcci.py
Author :      jynnezhang
Date:         2020/10/19 4:19 下午
Description:
"""

class Solution:
    def masterMind(self, solution: str, guess: str):
        if solution is None or len(solution) == 0:
            return [0, 0]
        result = [0, 0]
        for index, c in enumerate(guess):
            if c == solution[index]:
                result[0] += 1
                if index < len(guess):
                    guess = guess[:index] +" "+ guess[index + 1:]
                    solution = solution[:index] + " "+ solution[index + 1:]
                else:
                    guess = guess[:index] + " "
                    solution = solution[:index] + ""
        for index, c in enumerate(guess):
            if c != " " and c in solution:
                index_c = solution.index(c)
                result[1] += 1
                if index < len(guess):
                    guess = guess[:index] +" "+ guess[index + 1:]
                else:
                    guess = guess[:index] + ""
                if index_c < len(solution):
                    solution = solution[:index_c] +" "+ solution[index_c + 1:]
                else:
                    solution = solution[:index_c] + ""
        return result


if __name__ == '__main__':
    print(Solution().masterMind(solution="RGBY",guess="GGRR"))
