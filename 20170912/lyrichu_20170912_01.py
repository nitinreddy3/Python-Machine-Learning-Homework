#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/12 14:59
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : test.py
'''
@Description:
Q1:使用python实现二叉树，并写出中序遍历，前序遍历，后序遍历，以及层次遍历的结果。
'''

class Node(object):
  """节点类"""
  def __init__(self, elem=None, lchild=None, rchild=None):
    self.elem = elem
    self.lchild = lchild
    self.rchild = rchild

class Tree(object):
  """树类"""
  def __init__(self):
    self.root = Node()
    self.myQueue = []

  def add(self, elem):
    """为树添加节点"""
    node = Node(elem)
    if self.root.elem == None: # 如果树是空的，则对根节点赋值
      self.root = node
      self.myQueue.append(self.root)
    else:
      treeNode = self.myQueue[0] # 此结点的子树还没有齐。
      if treeNode.lchild == None:
        treeNode.lchild = node
        self.myQueue.append(treeNode.lchild)
      else:
        treeNode.rchild = node
        self.myQueue.append(treeNode.rchild)
        self.myQueue.pop(0) # 如果该结点存在右子树，将此结点丢弃。

  def front_recur(self, root):
    """利用递归实现树的先序遍历"""
    if root == None:
      return
    print root.elem,
    self.front_recur(root.lchild)
    self.front_recur(root.rchild)

  def middle_recur(self, root):
    """利用递归实现树的中序遍历"""
    if root == None:
      return
    self.middle_recur(root.lchild)
    print root.elem,
    self.middle_recur(root.rchild)

  def later_recur(self, root):
    """利用递归实现树的后序遍历"""
    if root == None:
      return
    self.later_recur(root.lchild)
    self.later_recur(root.rchild)
    print root.elem,

  def front_stack(self, root):
    """利用堆栈实现树的先序遍历"""
    if root == None:
      return
    myStack = []
    node = root
    while node or myStack:
      while node:           #从根节点开始，一直找它的左子树
        print node.elem,
        myStack.append(node)
        node = node.lchild
      node = myStack.pop()      #while结束表示当前节点node为空，即前一个节点没有左子树了
      node = node.rchild         #开始查看它的右子树

  def middle_stack(self, root):
    """利用堆栈实现树的中序遍历"""
    if root == None:
      return
    myStack = []
    node = root
    while node or myStack:
      while node:           #从根节点开始，一直找它的左子树
        myStack.append(node)
        node = node.lchild
      node = myStack.pop()      #while结束表示当前节点node为空，即前一个节点没有左子树了
      print node.elem,
      node = node.rchild         #开始查看它的右子树

  def later_stack(self, root):
    """利用堆栈实现树的后序遍历"""
    if root == None:
      return
    myStack1 = []
    myStack2 = []
    node = root
    myStack1.append(node)
    while myStack1:          #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
      node = myStack1.pop()
      if node.lchild:
        myStack1.append(node.lchild)
      if node.rchild:
        myStack1.append(node.rchild)
      myStack2.append(node)
    while myStack2:             #将myStack2中的元素出栈，即为后序遍历次序
      print myStack2.pop().elem,

  def level_queue(self, root):
    """利用队列实现树的层次遍历"""
    if root == None:
      return
    myQueue = []
    node = root
    myQueue.append(node)
    while myQueue:
      node = myQueue.pop(0)
      print node.elem,
      if node.lchild != None:
        myQueue.append(node.lchild)
      if node.rchild != None:
        myQueue.append(node.rchild)

if __name__ == '__main__':
  """主函数"""
  elems = range(10)      #生成十个数据作为树节点
  tree = Tree()     # 新建一个树对象
  for elem in elems:
    tree.add(elem)      #逐个添加树的节点
  print '队列实现层次遍历:'
  tree.level_queue(tree.root)
  print '\n递归实现先序遍历:'
  tree.front_recur(tree.root)
  print '\n递归实现中序遍历:'
  tree.middle_recur(tree.root)
  print '\n递归实现后序遍历:'
  tree.later_recur(tree.root)
  print '\n堆栈实现先序遍历:'
  tree.front_stack(tree.root)
  print '\n堆栈实现中序遍历:'
  tree.middle_stack(tree.root)
  print '\n堆栈实现后序遍历:'
  tree.later_stack(tree.root)





