"""
 * 给你一个整数数组 nums 。
 * 返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
"""
from typing import List


class Solution:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            j = i + 1
            while j < n:
                if nums[j] <= nums[j - 1]:
                    break
                j += 1
            ans = max(ans, j - i)
        for i in range(n):
            j = i + 1
            while j < n:
                if nums[j] >= nums[j - 1]:
                    break
                j += 1
            ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]))
    # 1
    print(Solution().longestMonotonicSubarray([3, 3, 3, 3]))
    # 3
    print(Solution().longestMonotonicSubarray([3, 2, 1]))
