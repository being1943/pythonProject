#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 14:10
@Author  : Caps
@File    : test
"""

x = 'a'


def outer_func():
    x = 'b'

    def inner_func():
        x = 'c'
        print('local:' + x)

    inner_func()
    print('nolocal:' + x)
    print('global:' + globals()['x'])

    def changelocal():
        nonlocal x
        x = 'changed nolocal'

    def changeglobal():
        global x
        x = 'changed global'

    changelocal()
    changeglobal()
    print('after changelocal:' + x)
    print('after changeglobal:' + globals()['x'])


outer_func()

if __name__ == '__main__':
    pass
