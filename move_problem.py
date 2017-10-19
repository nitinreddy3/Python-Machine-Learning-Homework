#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: move_problem.py
@Time: 2017/10/19 8:46
"""


def move(m, n):
    '''
    :param m: m行
    :param n: n列
    :return:  移动总次数
    '''
    if m == 1 or n == 1:
        return 1
    else:
        return move(m - 1, n) + move(m, n - 1)

if __name__ == '__main__':
    # m, n = 100
    m = 10
    n = 10
    print(move(m, n))