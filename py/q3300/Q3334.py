"""
 * 给你一个整数数组 nums。
 * 因子得分 定义为数组所有元素的最小公倍数（LCM）与最大公约数（GCD）的 乘积。
 * 在 最多 移除一个元素的情况下，返回 nums 的 最大因子得分。
 * 注意，单个数字的 LCM 和 GCD 都是其本身，而 空数组 的因子得分为 0。
 * lcm(a, b) 表示 a 和 b 的 最小公倍数。
 * gcd(a, b) 表示 a 和 b 的 最大公约数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 30
 * 链接：https://leetcode.cn/problems/find-the-maximum-factor-score-of-array
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

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0] ** 2
        lcm_l, lcm_r = [0] * n, [0] * n
        gcd_l, gcd_r = [0] * n, [0] * n
        for i in range(len(nums)):
            lcm_l[i] = lcm(nums[i], lcm_l[i - 1] if i > 0 else 1)
            gcd_l[i] = gcd(nums[i], gcd_l[i - 1] if i > 0 else nums[i])
        ans = lcm_l[-1] * gcd_l[-1]
        for i in range(len(nums) - 1, -1, -1):
            lcm_r[i] = lcm(nums[i], lcm_r[i + 1] if i < n - 1 else 1)
            gcd_r[i] = gcd(nums[i], gcd_r[i + 1] if i < n - 1 else nums[i])
            lcm_rr, lcm_ll = lcm_r[i + 1] if i < n - 1 else 1, lcm_l[i - 1] if i > 0 else 1
            gcd_rr, gcd_ll = gcd_r[i + 1] if i < n - 1 else -1, gcd_l[i - 1] if i > 0 else -1
            if gcd_ll == -1:
                gcd__ = gcd_rr
            elif gcd_rr == -1:
                gcd__ = gcd_ll
            else:
                gcd__ = gcd(gcd_rr, gcd_ll)
            ans = max(ans, lcm(lcm_ll, lcm_rr) * gcd__)
        return ans


if __name__ == '__main__':
    # 840
    print(Solution().maxScore([6, 14, 20]))
    # 64
    print(Solution().maxScore([2, 4, 8, 16]))
    # 60
    print(Solution().maxScore([1, 2, 3, 4, 5]))
    # 9
    print(Solution().maxScore([3]))
