"""
 * Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她 可能 在一个按键上按太久，导致一个字符被输入 多次 。
 * 尽管 Alice 尽可能集中注意力，她仍然可能会犯错 至多 一次。
 * 给你一个字符串 word ，它表示 最终 显示在 Alice 显示屏上的结果。
 * 请你返回 Alice 一开始可能想要输入字符串的总方案数。
 * 提示：
 * 1、1 <= word.length <= 100
 * 2、word 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-the-original-typed-string-i/
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for x, y in pairwise(word):
            if x == y:
                ans += 1
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().possibleStringCount("abbcccc"))
    # 1
    print(Solution().possibleStringCount("abcd"))
    # 4
    print(Solution().possibleStringCount("aaaa"))
