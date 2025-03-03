"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 pivot 。请你将 nums 重新排列，使得以下条件均成立：
 * 1、所有小于 pivot 的元素都出现在所有大于 pivot 的元素 之前 。
 * 2、所有等于 pivot 的元素都出现在小于和大于 pivot 的元素 中间 。
 * 3、小于 pivot 的元素之间和大于 pivot 的元素之间的 相对顺序 不发生改变。
 * 更正式的，考虑每一对 pi，pj ，pi 是初始时位置 i 元素的新位置，pj 是初始时位置 j 元素的新位置。如果 i < j 且两个元素 都 小于（或大于）pivot，那么 pi < pj 。
 * 请你返回重新排列 nums 数组后的结果数组。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^6 <= nums[i] <= 10^6
 * 3、pivot 等于 nums 中的一个元素。
 * 链接：https://leetcode.cn/problems/partition-array-according-to-given-pivot
"""

from typing import List
INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=2161 lang=python3
# @lcpr version=30008
#
# [2161] 根据给定数字划分数组
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        for num in nums:
            if num < pivot: ans.append(num)
        for num in nums:
            if num == pivot: ans.append(num)
        for num in nums:
            if num > pivot: ans.append(num)
        return ans
# @lc code=end





if __name__ == '__main__':
    # [9,5,3,10,10,12,14]
    print(Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
    # [-3,2,4,3]
    print(Solution().pivotArray([-3, 4, 3, 2] , 2))
