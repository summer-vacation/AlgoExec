# -*- coding: utf-8 -*-
"""
File Name:    11decorators.py
Author :      jynnezhang
Date:         2020/12/1 11:47 上午
Description:
"""


from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


hello()
