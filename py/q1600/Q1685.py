"""
 * 给你一个 非递减 有序整数数组 nums 。
 * 请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。
 * 换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （下标从 0 开始）。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= nums[i + 1] <= 10^4
 * 链接：https://leetcode.cn/problems/sum-of-absolute-differences-in-a-sorted-array
"""

from itertools import accumulate
from typing import List

#
# @lc app=leetcode.cn id=1685 lang=python3
#
# [1685] 有序数组中差绝对值之和
#


# @lc code=start
class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre_sum = [0] + list(accumulate(nums))
        ans, n = [], len(nums)
        for i, num in enumerate(nums):
            ans.append(pre_sum[-1] - pre_sum[i + 1] - num * (n - i - 1) + num * i - pre_sum[i])
        return ans


# @lc code=end

if __name__ == '__main__':
    # [4,3,5]
    print(Solution().getSumAbsoluteDifferences([2, 3, 5]))
    # [24,15,13,15,21]
    print(Solution().getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
    #
    # print(Solution().getSumAbsoluteDifferences())
