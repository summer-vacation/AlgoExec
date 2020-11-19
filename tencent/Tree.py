# -*- coding: utf-8 -*-
"""

   File Name：     Tree
   Author :       jing
   Date：          2020/3/23
"""
class Node(object):
    def __init__(self,e=None,lchild=None,rchild=None):
        self.e=e
        self.lchild=lchild
        self.rchild=rchild

# 树类
class Tree(object):
    def __init__(self, root=Node(None, None, None)):
        self.root = root
        self.height = 0
        self.MyQueue = []

    # 按层序添加节点到树中
    def add(self, e):
        node = Node(e)

        if self.root.e == None:
            self.root = node
            if not node == None:
                self.height += 1

            self.MyQueue.append(self.root)
        else:
            treeNode = self.MyQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                if not node == None:
                    self.height += 1

                self.MyQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node

                self.MyQueue.append(treeNode.rchild)
                self.MyQueue.pop(0)

    # 层序遍历
    def level(self):
        if self.root == None:
            return
        MQ = []
        node = self.root
        MQ.append(node)
        while MQ:
            node = MQ.pop(0)
            print(node.e)
            if node.lchild:
                MQ.append(node.lchild)
            if node.rchild:
                MQ.append(node.rchild)

    # 前序遍历
    def front(self, root):
        if root == None:
            return
        print(root.e)
        self.front(root.lchild)
        self.front(root.rchild)

    # 中序遍历
    def middle(self, root):
        if root == None:
            return
        self.middle(root.lchild)
        print(root.e)
        self.middle(root.rchild)

    # 后序遍历
    def post(self, root):
        if root == None:
            return
        self.post(root.lchild)
        self.post(root.rchild)
        print(root.e)



# 定义一个树节点
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left     # 左子树
        self.right = right   # 右子树

# 实例化一个树节点
node1 = TreeNode("A",
                 TreeNode("B",
                          TreeNode("D"),
                          TreeNode("E")
                          ),
                 TreeNode("C",
                          TreeNode("F"),
                          TreeNode("G")
                          )
                 )


# 前序遍历
def preTraverse(root):
    if root is None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


# 中序遍历
def midTraverse(root):
    if root is None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


# 后序遍历
def afterTraverse(root):
    if root is None:
        return
    afterTraverse(root.right)
    afterTraverse(root.left)
    print(root.value)

def levelOrder(root):
    # 如果根节点为空，则返回空列表
    res = []
    if root is None:
        return res
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            print(r.value)


if __name__ == "__main__":
    preTraverse(node1)
    print("------------------------")
    midTraverse(node1)
    print("------------------------")
    afterTraverse(node1)
