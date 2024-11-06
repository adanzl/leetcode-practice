"""
 * 给你一个字符串 s 和一个整数 t，表示要执行的 转换 次数。每次 转换 需要根据以下规则替换字符串 s 中的每个字符：
 * 1、如果字符是 'z'，则将其替换为字符串 "ab"。
 * 2、否则，将其替换为字母表中的下一个字符。例如，'a' 替换为 'b'，'b' 替换为 'c'，依此类推。
 * 返回 恰好 执行 t 次转换后得到的字符串的 长度。
 * 由于答案可能非常大，返回其对 10^9 + 7 取余的结果。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅由小写英文字母组成。
 * 3、1 <= t <= 10^5
 * 链接：https://leetcode.cn/problems/total-characters-in-string-after-transformations-i/
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

MOD = 10**9 + 7


class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for _ in range(t):
            cnt = [cnt[-1], (cnt[-1] + cnt[0]) % MOD] + cnt[1:-1]
        return sum(cnt) % MOD


if __name__ == '__main__':
    # 825415876
    print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", t=72388))
    # 7
    print(Solution().lengthAfterTransformations("abcyy", t=2))
    # 5
    print(Solution().lengthAfterTransformations("azbk", t=1))
