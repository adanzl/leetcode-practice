"""
 * 给你一个下标从 1 开始、由 n 个整数组成的数组。
 * 如果一组数字中每对元素的乘积都是一个完全平方数，则称这组数字是一个 完全集 。
 * 下标集 {1, 2, ..., n} 的子集可以表示为 {i1, i2, ..., ik}，我们定义对应该子集的 元素和 为 nums[i1] + nums[i2] + ... + nums[ik] 。
 * 返回下标集 {1, 2, ..., n} 的 完全子集 所能取到的 最大元素和 。
 * 完全平方数是指可以表示为一个整数和其自身相乘的数。
 * 提示：
 * 1、1 <= n == nums.length <= 10^4
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-element-sum-of-a-complete-subset-of-indices/
"""
from collections import Counter
from functools import cache
from itertools import count
import math
from typing import List


@cache
def core(num):  # 返回num去除完全平方因子之后的结果
    res = 1
    for i in range(2, math.isqrt(num) + 1):
        e = 0
        while num % i == 0:
            e ^= 1
            num //= i
        if e: res *= i
    if num > 1: res *= num
    return res


class Solution:

    def maximumSum1(self, nums: List[int]) -> int:
        s = Counter()
        for i, x in enumerate(nums, 1):
            s[core(i)] += x
        return max(s.values())

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            vv = 0
            for j in count(1):
                idx = (1 + i) * j * j - 1
                if idx >= n: break
                vv += nums[idx]
            ans = max(ans, vv)
        return ans


if __name__ == '__main__':
    # 97
    print(Solution().maximumSum([35, 45, 29, 16, 42, 49, 25, 19, 46]))
    # 100
    print(Solution().maximumSum([1, 100, 100, 1]))
    # 19
    print(Solution().maximumSum([5, 10, 3, 10, 1, 13, 7, 9, 4]))
    # 16
    print(Solution().maximumSum([8, 7, 3, 5, 7, 2, 4, 9]))
