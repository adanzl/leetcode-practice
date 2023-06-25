"""
 * 给你一个 正 整数数组 nums 。
 * 将 nums 分成两个数组：nums1 和 nums2 ，并满足下述条件：
 * 1、数组 nums 中的每个元素都属于数组 nums1 或数组 nums2 。
 * 2、两个数组都 非空 。
 * 3、分区值 最小 。
 * 分区值的计算方法是 |max(nums1) - min(nums2)| 。
 * 其中，max(nums1) 表示数组 nums1 中的最大元素，min(nums2) 表示数组 nums2 中的最小元素。
 * 返回表示分区值的整数。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-value-of-the-partition/
"""
from typing import List


class Solution:

    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = 10**10
        for i in range(len(nums) - 1):
            ans = min(ans, nums[i + 1] - nums[i])
        return ans


if __name__ == '__main__':
    #
    print(Solution().findValueOfPartition([1, 3, 2, 4]))
    #
    print(Solution().findValueOfPartition([1, 10, 100]))
