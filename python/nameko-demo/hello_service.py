# -*- coding: utf-8 -*-
"""
File Name:    hello_service.py
Author :      jynnezhang
Date:         2020/12/15 9:29 上午
Description:
"""

from nameko.rpc import rpc


class hello_service:
    name = "hello_service"

    @rpc
    def hello(self):
        print("hello world")
