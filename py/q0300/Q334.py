"""
 * 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
 * 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
 * 链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
"""
from typing import List


class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        mn1 = mn2 = 2**31
        for num in nums:
            if num >mn2:
                return True
            if num > mn1:
                mn2 = min(mn2, num)
            mn1 = min(mn1, num)
        return False


if __name__ == '__main__':
    # False
    print(Solution().increasingTriplet([1, 1, -2, 6]))
    # True
    print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
    # False
    print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
    # True
    print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
