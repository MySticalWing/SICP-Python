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
              f(n - 1) + 2*f(n - 2) + 3*f(n - 3) if n >= 3
implement f(n) by recursive and iterative method
"""


@lru_cache()  # better performance
def recursive_fn(n: int):
    if n < 3:
        return n

    return recursive_fn(n - 1) + 2 * recursive_fn(n - 2) + 3 * recursive_fn(n - 3)


def iterative_fn(n: int):
    if n < 3:
        return n

    a, b, c = 2, 1, 0

    for _ in range(2, n):
        tmp = a + 2 * b + 3 * c
        a, b, c = tmp, a, b

    return a


if __name__ == '__main__':
    num = 1000

    for i in range(100):
        assert recursive_fn(i) == iterative_fn(i)
        print(iterative_fn(i))

    print(iterative_fn(n=10000))
