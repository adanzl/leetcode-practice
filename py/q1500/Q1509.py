"""
 * 给你一个数组 nums 。
 * 每次操作你可以选择 nums 中的任意一个元素并将它改成 任意值 。
 * 在 执行最多三次移动后 ，返回 nums 中最大值与最小值的最小差值。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
"""

from typing import List

#
# @lc app=leetcode.cn id=1509 lang=python3
#
# [1509] 三次操作后最大值与最小值的最小差
#


# @lc code=start
class Solution:

    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        n = len(nums)
        if n <= 3: return 0
        for i in range(4):
            ans = min(ans, nums[n - 4 + i] - nums[i])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().minDifference([5, 3, 2, 4]))
    # 1
    print(Solution().minDifference([1, 5, 0, 10, 14]))
    # 0
    print(Solution().minDifference([3, 100, 20]))
