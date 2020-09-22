# -*- coding: utf-8 -*-
"""
File Name:    requests-02.py
Author :      jynnezhang
Date:         2020/4/27 3:54 下午
Description:
"""


import requests
parameters = {'q': 'Python', 'client': 'Firefox'}
response = requests.get('http://www.google.com/search', params=parameters)
print('actual URL:', response.url)
print(response.content)
