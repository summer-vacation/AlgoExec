# -*- coding: utf-8 -*-
"""
   File Name：     str_to_exp
   Author :       jing
   Date：          2020/4/13

   有一个字符串，它是一个数值表达式，如：1*2+3/5+7，
   其中操作符只有加、减、乘、除四种，没有括号，运算对象为数字。
   请处理该字符串，得到表达式的运算结果。（注意操作符的优先级）
"""


def str_to_exp(input):
    if str is None or len(input) == 0:
        return None

    return eval(input)


print(str_to_exp("1*2+2/1"))
print(str_to_exp("1*2+3/5+7"))
