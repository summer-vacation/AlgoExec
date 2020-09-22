# -*- coding: utf-8 -*-
"""
File Name:    utils.py
Author :      jynnezhang
Date:         2020/4/27 3:34 下午
Description:
"""


def toByte(input):
    if type(input) is str:
        return input.encode('utf8')
    return input
