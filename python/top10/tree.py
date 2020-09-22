# -*- coding: utf-8 -*-
"""
File Name:    tree.py
Author :      jynnezhang
Date:         2020/9/10 1:09 下午
Description:
"""


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
