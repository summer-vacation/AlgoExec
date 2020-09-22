# -*- coding: utf-8 -*-
"""
File Name:    deep_visit.py
Author :      jynnezhang
Date:         2020/9/10 1:09 下午
Description:  深度优先遍历
"""
from python.top10.tree import Node


def deep_visit_stack(root):
    """栈实现：深度遍历二叉树"""
    if not root:
        return
    stack = [root]
    while stack:
        # list.pop默认移除最后一个元素
        current = stack.pop()
        print(current.data, end=',')
        # 先右结点入
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


def deep_visit(root):
    """深度遍历二叉树"""
    if not root: return
    print(root.data, end=",")
    deep_visit(root.left)
    deep_visit(root.right)


tree = Node(
    1,
    Node(
        2,
        Node(4),
        Node(5,Node(7), Node(8))),
    Node(3,
         Node(6))
)
deep_visit_stack(tree)
deep_visit(tree)
