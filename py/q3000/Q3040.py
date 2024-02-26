"""
 * 给你一个整数数组 nums ，如果 nums 至少 包含 2 个元素，你可以执行以下操作中的 任意 一个：
 * 1、选择 nums 中最前面两个元素并且删除它们。
 * 2、选择 nums 中最后两个元素并且删除它们。
 * 3、选择 nums 中第一个和最后一个元素并且删除它们。
 * 一次操作的 分数 是被删除元素的和。
 * 在确保 所有操作分数相同 的前提下，请你求出 最多 能进行多少次操作。
 * 请你返回按照上述要求 最多 可以进行的操作次数。
 * 提示：
 * 1、2 <= nums.length <= 2000
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/
"""
from functools import cache
from typing import List


class Solution:

    def maxOperations(self, nums: List[int]) -> int:

        @cache
        def func(l, r, sm):
            if r - l < 1: return 0
            ret = 0
            if sm == nums[l] + nums[l + 1]:
                ret = max(ret, func(l + 2, r, sm) + 1)
            if sm == nums[l] + nums[r]:
                ret = max(ret, func(l + 1, r - 1, sm) + 1)
            if sm == nums[r - 1] + nums[r]:
                ret = max(ret, func(l, r - 2, sm) + 1)
            return ret

        n = len(nums)
        if n < 2: return 0
        return max(
            func(2, n - 1, nums[0] + nums[1]),
            func(0, n - 3, nums[-1] + nums[-2]),
            func(1, n - 2, nums[0] + nums[-1]),
        ) + 1


if __name__ == '__main__':
    # 3
    print(Solution().maxOperations([3, 2, 1, 2, 3, 4]))
    # 2
    print(Solution().maxOperations([3, 2, 6, 1, 4]))
    #
    # print(Solution().maxOperations())
