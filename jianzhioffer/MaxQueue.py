# -*- coding: utf-8 -*-
"""
File Name:    MaxQueue.py
Author :      jynnezhang
Date:         2020/4/29 11:21 上午
Description:

时间复杂度都是o(1)
"""

import queue


class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


maxqueue = MaxQueue()
maxqueue.push_back(4)
maxqueue.push_back(2)
maxqueue.push_back(3)
maxqueue.push_back(5)
maxqueue.max_value()
maxqueue.pop_front()
maxqueue.pop_front()
maxqueue.push_back(4)
maxqueue.pop_front()



