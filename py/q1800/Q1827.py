"""
 * 给你一个整数数组 nums （下标从 0 开始）。每一次操作中，你可以选择数组中一个元素，并将它增加 1 。
 * 比方说，如果 nums = [1,2,3] ，你可以选择增加 nums[1] 得到 nums = [1,3,3] 。
 * 请你返回使 nums 严格递增 的 最少 操作次数。
 * 我们称数组 nums 是 严格递增的 ，当它满足对于所有的 0 <= i < nums.length - 1 都有 nums[i] < nums[i+1] 。
 * 一个长度为 1 的数组是严格递增的一种特殊情况。
 * 提示：
 * 1、1 <= nums.length <= 5000
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            val = max(nums[i - 1] + 1 - nums[i], 0)
            ans += val
            nums[i] += val
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minOperations([1, 1, 1]))
    # 14
    print(Solution().minOperations([1, 5, 2, 4, 1]))
    # 0
    print(Solution().minOperations([8]))
