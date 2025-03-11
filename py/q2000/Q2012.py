"""
 * 给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：
 * 1、2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
 * 2、1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
 * 3、0，如果上述条件全部不满足
 * 返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/sum-of-beauty-in-the-array
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
# @lc app=leetcode.cn id=2012 lang=python3
# @lcpr version=30101
#
# [2012] 数组美丽值求和
#


# @lc code=start
class Solution:

    def sumOfBeauties(self, nums: List[int]) -> int:
        ans = 0
        mx_l = [nums[0]]
        mn_r = nums[-1]
        for i in range(1, len(nums)):
            mx_l.append(max(mx_l[-1], nums[i]))
        for i in range(len(nums) - 2, 0, -1):
            if mx_l[i - 1] < nums[i] < mn_r:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
            mn_r = min(mn_r, nums[i])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().sumOfBeauties([2, 4, 6, 4]))
    # 2
    print(Solution().sumOfBeauties([1, 2, 3]))
    # 0
    print(Solution().sumOfBeauties([3, 2, 1]))
