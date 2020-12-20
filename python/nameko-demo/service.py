# -*- coding: utf-8 -*-
"""
File Name:    service.py
Author :      jynnezhang
Date:         2020/12/15 9:29 上午
Description:
python3 -m pip install nameko
"""

from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://guest:guest@0.0.0.0"}


def compute():
    with ClusterRpcProxy(CONFIG) as rpc:
        rpc.hello_service.hello()


if __name__ == '__main__':
    compute()

