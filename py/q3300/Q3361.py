"""
 * 给你两个长度相同的字符串 s 和 t ，以及两个整数数组 nextCost 和 previousCost 。
 * 一次操作中，你可以选择 s 中的一个下标 i ，执行以下操作 之一 ：
 * 1、将 s[i] 切换为字母表中的下一个字母，如果 s[i] == 'z' ，切换后得到 'a' 。操作的代价为 nextCost[j] ，其中 j 表示 s[i] 在字母表中的下标。
 * 2、将 s[i] 切换为字母表中的上一个字母，如果 s[i] == 'a' ，切换后得到 'z' 。操作的代价为 previousCost[j] ，其中 j 是 s[i] 在字母表中的下标。
 * 切换距离 指的是将字符串 s 变为字符串 t 的 最少 操作代价总和。
 * 请你返回从 s 到 t 的 切换距离 。
 * 提示：
 * 1、1 <= s.length == t.length <= 10^5
 * 2、s 和 t 都只包含小写英文字母。
 * 3、nextCost.length == previousCost.length == 26
 * 4、0 <= nextCost[i], previousCost[i] <= 10^9
 * 链接：https://leetcode.cn/problems/shift-distance-between-two-strings/description/
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

    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        ans = 0

        @cache
        def trans(a, b):  # a->b
            if a < b:
                v1 = sum(nextCost[a:b])
                v2 = sum(previousCost[:a + 1]) + sum(previousCost[b + 1:])
            else:
                v1 = sum(previousCost[b + 1:a + 1])
                v2 = sum(nextCost[a:]) + sum(nextCost[:b])
            return min(v1, v2)

        for a, b in zip(s, t):
            if a == b: continue
            ans += trans(ord(a) - ord('a'), ord(b) - ord('a'))
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().shiftDistance(
        "abab",
        t="baba",
        nextCost=[100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        previousCost=[1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # 31
    print(Solution().shiftDistance(
        "leet",
        t="code",
        nextCost=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        previousCost=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    #
    # print(Solution().shiftDistance())
