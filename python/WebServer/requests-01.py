# -*- coding: utf-8 -*-
"""
File Name:    requests-01.py
Author :      jynnezhang
Date:         2020/4/27 3:51 下午
Description:
"""


import requests

response = requests.get("http://aosabook.org/en/posa/introduction.html")
print('status code:', response.status_code)
print('content length:', response.headers['content-length'])
print(response.text)
