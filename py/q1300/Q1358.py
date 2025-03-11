"""
 * 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
 * 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
 * 提示：
 * 1、3 <= s.length <= 5 x 10^4
 * 2、s 只包含字符 a，b 和 c 。
 * 链接：https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters
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

#
# @lc app=leetcode.cn id=1358 lang=python3
# @lcpr version=30101
#
# [1358] 包含所有三种字符的子字符串数目
#


# @lc code=start
class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        l_idx = {'a': -1, 'b': -1, 'c': -1}
        for i, c in enumerate(s):
            l_idx[c] = i
            ans += min(l_idx.values()) + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 10
    print(Solution().numberOfSubstrings("abcabc"))
    # 3
    print(Solution().numberOfSubstrings("aaacb"))
    # 1
    print(Solution().numberOfSubstrings("abc"))
