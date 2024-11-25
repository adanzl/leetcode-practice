"""
 * 给你一个由 n 个整数组成的数组 nums ，请你找出 k 的 最大值，使得存在 两个 相邻 且长度为 k 的 严格递增 子数组。
 * 具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：
 * 1、这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
 * 2、这两个子数组必须是 相邻的，即 b = a + k。
 * 返回 k 的 最大可能 值。
 * 子数组 是数组中的一个连续 非空 的元素序列。
 * 提示：
 * 1、2 <= nums.length <= 2 * 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/adjacent-increasing-subarrays-detection-ii
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

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1]
        ans = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                f.append(f[-1] + 1)
            else:
                f.append(1)
        for i in range(n):
            lo, hi = 0, min(f[i] + 1, n - i)
            while lo < hi:
                mid = (lo + hi) // 2
                ff = f[i + mid] >= mid
                if ff:
                    lo = mid + 1
                    ans = max(ans, mid)
                else:
                    hi = mid
        return ans

    def maxIncreasingSubarrays1(self, nums: List[int]) -> int:
        ans = pre_cnt = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == len(nums) - 1 or x >= nums[i + 1]:  # i 是严格递增段的末尾
                ans = max(ans, cnt // 2, min(pre_cnt, cnt))
                pre_cnt = cnt
                cnt = 0
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
    # 1
    print(Solution().maxIncreasingSubarrays1([3, 6, 15, 15, -15, 8]))
    # 3
    print(Solution().maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
