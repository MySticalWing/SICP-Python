#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/18 上午9:47
@Author:  qin_hw
@File: 1.11.py
@Software: PyCharm
"""

from functools import lru_cache

"""
define f(n) = n if n < 3
              f(n - 1) + 2*f(n - 2) + 3*f(n - 3) if n <= 3
implement f(n) by recursive and iterative method
"""


@lru_cache()  # better performance
def recursive_fn(n: int):
    if n < 3:
        return n

    return recursive_fn(n - 1) + 2 * recursive_fn(n - 2) + 3 * recursive_fn(n - 3)


def raw_iterative_fn(n: int):
    if n < 3:
        return n

    def _iter(a, b, c, n1):
        if n1 < 3:
            return a
        return _iter(a + 2 * b + c * 3, a, b, n1 - 1)

    return _iter(2, 1, 0, n)


def stack_iterative_fn(n: int):
    if n < 3:
        return n

    class Stack(object):
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            return self.stack.pop()

        def empty(self):
            return len(self.stack) == 0

        def size(self):
            return len(self.stack)

    stack = Stack()
    stack.push((2, 1, 0, n))

    while not stack.empty():
        a, b, c, n1 = stack.pop()

        if n1 < 3:
            return a

        stack.push((a + 2 * b + 3 * c, a, b, n1 - 1))


if __name__ == '__main__':
    num = 100
    print(recursive_fn(num))
    print(raw_iterative_fn(num))
    print(stack_iterative_fn(num))
