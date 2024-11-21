"""
 * 给你一个由 n 个整数组成的数组 nums 和一个整数 k，请你确定是否存在 两个 相邻 且长度为 k 的 严格递增 子数组。
 * 具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：
 * 1、这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
 * 2、这两个子数组必须是 相邻的，即 b = a + k。
 * 如果可以找到这样的 两个 子数组，请返回 true; 否则返回 false。
 * 子数组 是数组中的一个连续 非空 的元素序列。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= 2 * k <= nums.length
 * 3、-1000 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/adjacent-increasing-subarrays-detection-i/description/
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

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        f = [1]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                f.append(f[-1] + 1)
            else:
                f.append(1)
            if f[i] >= k and i >= k and f[i - k] >= k:
                return True
        return False


if __name__ == '__main__':
    # True
    print(Solution().hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
    # False
    print(Solution().hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
