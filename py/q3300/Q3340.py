"""
 * 给你一个仅由数字 0 - 9 组成的字符串 num。如果偶数下标处的数字之和等于奇数下标处的数字之和，则认为该数字字符串是一个 平衡字符串。
 * 如果 num 是一个 平衡字符串，则返回 true; 否则，返回 false。
 * 提示：
 * 1、2 <= num.length <= 100
 * 2、num 仅由数字 0 - 9 组成。
 * 链接：https://leetcode.cn/problems/check-balanced-string
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

    def isBalanced(self, num: str) -> bool:
        v0, v1 = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                v0 += int(num[i])
            else:
                v1 += int(num[i])
        return v0 == v1


if __name__ == '__main__':
    # False
    print(Solution().isBalanced("1234"))
    # True
    print(Solution().isBalanced("24123"))
    #
    # print(Solution().isBalanced())
