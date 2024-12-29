"""
 * 给你一个整数数组 nums。好子序列 的定义是：子序列中任意 两个 连续元素的绝对差 恰好 为 1。
 * 子序列 是指可以通过删除某个数组的部分元素（或不删除）得到的数组，并且不改变剩余元素的顺序。
 * 返回 nums 中所有 可能存在的 好子序列的 元素之和。
 * 因为答案可能非常大，返回结果需要对 10^9 + 7 取余。
 * 注意，长度为 1 的子序列默认为好子序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/sum-of-good-subsequences/
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

    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        ans = 0
        vv, cnt = Counter(), Counter()
        for num in nums:
            aa = (num + vv[num - 1] + num * cnt[num - 1] + vv[num + 1] + num * cnt[num + 1]) % MOD
            cnt[num] += 1 + cnt[num - 1] + cnt[num + 1]
            vv[num] = (vv[num] + aa) % MOD
            ans = (ans + aa) % MOD
        return ans


if __name__ == '__main__':
    # 14
    print(Solution().sumOfGoodSubsequences([1, 2, 1]))
    # 40
    print(Solution().sumOfGoodSubsequences([3, 4, 5]))
