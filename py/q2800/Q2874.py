"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。
 * 下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/
"""
from typing import List


class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, mx, mx_a = 0, 0, 0
        for i in range(2, len(nums)):
            mx = max(mx, nums[i - 2])
            mx_a = max(mx_a, mx - nums[i - 1])
            ans = max(ans, mx_a * nums[i])
        return ans


if __name__ == '__main__':
    # 266
    print(Solution().maximumTripletValue([8, 6, 3, 13, 2, 12, 19, 5, 19, 6, 10, 11, 9]))
    # 77
    print(Solution().maximumTripletValue([12, 6, 1, 2, 7]))
    # 133
    print(Solution().maximumTripletValue([1, 10, 3, 4, 19]))
    # 0
    print(Solution().maximumTripletValue([1, 2, 3]))
