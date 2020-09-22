# -*- coding: utf-8 -*-
"""

   File Name：     zigzag_conversion
   Author :       jing
   Date：          2020/3/16

   
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None or len(s) == 0 or numRows < 1:
            return s
        else:
            result = [""] * numRows         # 类似一个for循环，创建了["", "", ""]
            # for i in range(numRows):
            #     result.append("")
            j = 0
            for char in s:
                if j == numRows + numRows - 2:
                    j = 0
                if j >= numRows:
                    result[2*numRows - j - 2] = result[2*numRows - j - 2] + char
                    j = j + 1
                    continue
                result[j] = result[j] + char
                j += 1
        # out = ""
        # for i in range(len(result)):
        #     for j in range(len(result[i])):
        #         out = out + result[i][j]

        # join: str.join(seq), 用str拼接seq序列，eg： "-".join(["q", "e", "r"])   ->  q-e-r
        return "".join(result)

    def convert2(self, s, numRows):
        result = [''] * numRows

        j = 0
        for i in s:
            result[j] = result[j] + i
            if j == 0:
                m = j
                j += 1
            elif (j == numRows - 1) | (j - m < 0):
                m = j
                j -= 1
            else:
                m = j
                j += 1
        return ("".join(result))


if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 4))
