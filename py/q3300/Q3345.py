"""
 * 给你两个整数 n 和 t 。请你返回大于等于 n 的 最小 整数，且该整数的 各数位之积 能被 t 整除。
 * 提示：
 * 1、1 <= n <= 100
 * 2、1 <= t <= 10
 * 链接：https://leetcode.cn/problems/smallest-divisible-digit-product-i/
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, \
    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def smallestNumber(self, n: int, t: int) -> int:
        for v in range(n, 1000000):
            mul = 1
            for c in str(v):
                mul *= int(c)
            if mul % t == 0:
                return v
        return -1


if __name__ == '__main__':
    # 10
    print(Solution().smallestNumber(10, t=2))
    # 16
    print(Solution().smallestNumber(15, t=3))
