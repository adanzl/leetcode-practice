"""
 * 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和一个整数 k 。
 * 你可以执行下述 递增 运算 任意 次（可以是 0 次）：
 * 从范围 [0, n - 1] 中选择一个下标 i ，并将 nums[i] 的值加 1 。
 * 如果数组中任何长度 大于或等于 3 的子数组，其 最大 元素都大于或等于 k ，则认为数组是一个 美丽数组 。
 * 以整数形式返回使数组变为 美丽数组 需要执行的 最小 递增运算数。
 * 子数组是数组中的一个连续 非空 元素序列。
 * 提示：
 * 1、3 <= n == nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-increment-operations-to-make-array-beautiful/description/
"""
from typing import List


class Solution:

    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [10**100] * n
        for i, num in enumerate(nums):
            for j in range(max(i - 2, 0), i + 1):
                dp[i + 1] = min(dp[i + 1], dp[j])
            dp[i + 1] += max(0, k - num)
        return min(dp[-3:])


if __name__ == '__main__':
    # 2
    print(Solution().minIncrementOperations([0, 1, 3, 3], k=5))
    # 3
    print(Solution().minIncrementOperations([2, 3, 0, 0, 2], k=4))
    # 117
    print(Solution().minIncrementOperations([13, 34, 0, 13, 9, 19], 82))
    # 0
    print(Solution().minIncrementOperations([1, 1, 2], k=1))
