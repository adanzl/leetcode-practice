"""
 * Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她 可能 在一个按键上按太久，导致一个字符被输入 多次 。
 * 给你一个字符串 word ，它表示 最终 显示在 Alice 显示屏上的结果。
 * 同时给你一个 正 整数 k ，表示一开始 Alice 输入字符串的长度 至少 为 k 。
 * 请你返回 Alice 一开始可能想要输入字符串的总方案数。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= word.length <= 5 * 10^5
 * 2、word 只包含小写英文字母。
 * 3、1 <= k <= 2000
 * 链接：https://leetcode.cn/problems/find-the-original-typed-string-ii
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

    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:  # 无法满足要求
            return 0

        MOD = 1_000_000_007
        cnt_s = []
        ans = 1
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                if len(cnt_s) < k:
                    cnt_s.append(cnt)
                ans = ans * cnt % MOD
                cnt = 0

        m = len(cnt_s)
        if m >= k:  # 任何输入的字符串都至少为 k
            return ans

        f = [[0] * k for _ in range(m + 1)]
        f[0][0] = 1
        for i, c in enumerate(cnt_s):
            s = list(accumulate(f[i], initial=0))
            # j <= i 的 f[i][j] 都是 0
            for j in range(i + 1, k):
                f[i + 1][j] = (s[j] - s[max(j - c, 0)]) % MOD
        return (ans - sum(f[m][m:])) % MOD


if __name__ == '__main__':
    # 2
    print(Solution().possibleStringCount("duu", k=2))
    # 8
    print(Solution().possibleStringCount("aaabbb", k=3))
    # 5
    print(Solution().possibleStringCount("aabbccdd", k=7))
    # 1
    print(Solution().possibleStringCount("aabbccdd", k=8))
