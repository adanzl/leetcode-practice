"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。
 * 下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。
 * 提示：
 * 1、3 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-i/
"""
from typing import List


class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans


if __name__ == '__main__':
    # 77
    print(Solution().maximumTripletValue([12, 6, 1, 2, 7]))
    # 133
    print(Solution().maximumTripletValue([1, 10, 3, 4, 19]))
    # 0
    print(Solution().maximumTripletValue([1, 2, 3]))
