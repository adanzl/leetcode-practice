"""
 * 给你两个下标从 0 开始的数组 nums1 和 nums2 ，两个数组都只包含非负整数。
 * 请你求出另外一个数组 nums3 ，包含 nums1 和 nums2 中 所有数对 的异或和（nums1 中每个整数都跟 nums2 中每个整数 恰好 匹配一次）。
 * 请你返回 nums3 中所有整数的 异或和 。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 10^5
 * 2、0 <= nums1[i], nums2[j] <= 10^9
 * 链接：https://leetcode.cn/problems/bitwise-xor-of-all-pairings/
"""
from functools import reduce
from operator import xor
from typing import *


class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        ans = 0
        if l1 % 2 != 0: ans ^= reduce(xor, nums2)
        if l2 % 2 != 0: ans ^= reduce(xor, nums1)
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().xorAllNums([2, 1, 3], [10, 2, 5, 0]))
    # 0
    print(Solution().xorAllNums([1, 2], [3, 4]))
