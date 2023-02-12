"""
 * 给你一个整数数组 nums 。一个子数组 [num1, nums2, ...] 的 和的绝对值 为 abs(nums1 + nums2 + ... ) 。
 * 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
 * abs(x) 定义如下：
 * 1、如果 x 是负整数，那么 abs(x) = -x 。
 * 2、如果 x 是非负整数，那么 abs(x) = x 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
"""
from itertools import accumulate
from typing import List


class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 任意子数组和的绝对值的最大值 = 前缀和数组最大值 - 前缀和数组最小值
        preSum = [0] + list(accumulate(nums))
        return max(preSum) - min(preSum)

    def maxAbsoluteSum1(self, nums: List[int]) -> int:
        dp = [nums[0], nums[0]]
        n = len(nums)
        ans = abs(nums[0])
        for i in range(1, n):
            dp = [max(dp[0] + nums[i], nums[i]), min(dp[1] + nums[i], nums[i])]
            ans = max(ans, abs(dp[0]), abs(dp[1]))
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().maxAbsoluteSum([-1]))
    # 5
    print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]))
    # 8
    print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]))