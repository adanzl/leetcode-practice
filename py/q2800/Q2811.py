"""
 * 给你一个长度为 n 的数组 nums 和一个整数 m 。请你判断能否执行一系列操作，将数组拆分成 n 个 非空 数组。
 * 在每一步操作中，你可以选择一个 长度至少为 2 的现有数组（之前步骤的结果） 并将其拆分成 2 个子数组，而得到的 每个 子数组，至少 需要满足以下条件之一：
 * 1、子数组的长度为 1 ，或者
 * 2、子数组元素之和 大于或等于  m 。
 * 如果你可以将给定数组拆分成 n 个满足要求的数组，返回 true ；否则，返回 false 。
 * 注意：子数组是数组中的一个连续非空元素序列。
 * 提示：
 * 1、1 <= n == nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、1 <= m <= 200
 * 链接：https://leetcode.cn/problems/check-if-it-is-possible-to-split-array/
"""
from functools import cache
from itertools import accumulate
from typing import List


class Solution:

    def canSplitArray(self, nums: List[int], m: int) -> bool:

        pre_sum = [0] + list(accumulate(nums))

        @cache
        def check(l, r):
            if l == r:
                return True
            if pre_sum[r + 1] - pre_sum[l] < m:
                return False
            for i in range(l, r):
                if check(l, i) and check(i + 1, r):
                    return True
            return False

        if len(nums) <= 2: return True
        for i in range(len(nums)):
            if check(0, i) and check(i + 1, len(nums) - 1):
                return True
        return False


if __name__ == '__main__':
    # True
    print(Solution().canSplitArray([1], 1))
    # True
    print(Solution().canSplitArray([1, 1], 3))
    # True
    print(Solution().canSplitArray([2, 2, 1], m=4))
    # False
    print(Solution().canSplitArray([2, 1, 3], m=5))
    # True
    print(Solution().canSplitArray([2, 3, 3, 2, 3], m=6))
