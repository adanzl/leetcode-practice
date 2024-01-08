"""
 * 如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增 ，那么我们称这个子数组为 移除递增 子数组。
 * 比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。
 * 请你返回 nums 中 移除递增 子数组的总数目。
 * 注意 ，剩余元素为空的数组也视为是递增的。
 * 子数组 指的是一个数组中一段连续的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/
"""
from typing import List


class Solution:

    def incRemovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i == n - 1:  # 每个非空子数组都可以移除
            return n * (n + 1) // 2
        ans = i + 2
        j = n - 1
        while j == n - 1 or nums[j] < nums[j + 1]:
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
            ans += i + 2
            j -= 1
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().incRemovableSubarrayCount([1, 2, 3, 4]))
    # 7
    print(Solution().incRemovableSubarrayCount([6, 5, 7, 8]))
    # 3
    print(Solution().incRemovableSubarrayCount([8, 7, 6, 6]))
