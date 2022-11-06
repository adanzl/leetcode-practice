"""
 * 给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：
 * 1、子数组的长度是 k，且
 * 2、子数组中的所有元素 各不相同 。
 * 返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。
 * 子数组 是数组中一段连续非空的元素序列。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/
"""
from typing import Counter, List


class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0] * (len(nums) + 1)
        c = Counter()
        d_cnt, ans = 0, 0
        for i, num in enumerate(nums):
            pre_sum[i + 1] = num + pre_sum[i]
            c[num] += 1
            if c[num] > 1: d_cnt += 1
            if i >= k:
                c[nums[i - k]] -= 1
                if c[nums[i - k]] >= 1: d_cnt -= 1
            if i >= k - 1 and d_cnt == 0:
                ans = max(ans, pre_sum[i + 1] - pre_sum[i - k + 1])
        return ans


if __name__ == '__main__':
    # 24
    print(Solution().maximumSubarraySum([1, 1, 1, 7, 8, 9], 3))
    # 3
    print(Solution().maximumSubarraySum([1, 2, 2], 2))
    # 15
    print(Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], k=3))
    # 0
    print(Solution().maximumSubarraySum([4, 4, 4], k=3))
