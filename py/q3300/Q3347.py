"""
 * 给你一个整数数组 nums 和两个整数 k 和 numOperations 。
 * 你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
 * 1、选择一个下标 i ，它在之前的操作中 没有 被选择过。
 * 2、将 nums[i] 增加范围 [-k, k] 中的一个整数。
 * 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
 * 一个元素 x 的 频率 指的是它在数组中出现的次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^9
 * 4、0 <= numOperations <= nums.length
 * 链接：https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
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

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ans = 0
        nums.sort()
        cnt = []
        for i, num in enumerate(nums):
            if cnt and cnt[-1][0] == num:
                cnt[-1][2] = i
            else:
                cnt.append([num, i, i])
        l, r = 0, 0
        while r < len(nums):
            while r < len(nums) and nums[r] - nums[l] <= k * 2:
                r += 1
            ans = max(ans, min(r - l, numOperations))
            l += 1
        for num, s, e in cnt:
            l_i = bisect_left(nums, num - k)
            r_i = bisect_right(nums, num + k) - 1
            ans = max(ans, e - s + 1 + min(numOperations, s - l_i + r_i - e))
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxFrequency([5, 11, 20, 20], k=5, numOperations=1))
    # 2
    print(Solution().maxFrequency([1, 4, 5], k=1, numOperations=2))
    #
    # print(Solution().maxFrequency())
