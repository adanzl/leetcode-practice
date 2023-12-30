"""
 * 给你一个下标从 0 开始的 正 整数数组 nums 。
 * 如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增 ，那么我们称这个子数组为 移除递增 子数组。
 * 比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。
 * 请你返回 nums 中 移除递增 子数组的总数目。
 * 注意 ，剩余元素为空的数组也视为是递增的。
 * 子数组 指的是一个数组中一段连续的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/
"""
from typing import List


class Solution:

    def incRemovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for l in range(n):
            for r in range(l, n):
                valid = True
                pre = 0
                for i in range(n):
                    if i < l or i > r:
                        if nums[i] <= pre:
                            valid = False
                            break
                        pre = nums[i]
                if valid:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().incRemovableSubarrayCount([8, 7, 6, 6]))
    # 7
    print(Solution().incRemovableSubarrayCount([6, 5, 7, 8]))
    # 10
    print(Solution().incRemovableSubarrayCount([1, 2, 3, 4]))
