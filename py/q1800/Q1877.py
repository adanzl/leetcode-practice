"""
 * 一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。
 * 比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
 * 给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：
 * 1、nums 中每个元素 恰好 在 一个 数对中，且
 * 2、最大数对和 的值 最小 。
 * 请你在最优数对划分的方案下，返回最小的 最大数对和 。
 * 提示：
 * 1、n == nums.length
 * 2、2 <= n <= 10^5
 * 3、n 是 偶数 。
 * 4、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array
"""

from typing import List

#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#


# @lc code=start
class Solution:

    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 8
    print(Solution().minPairSum([4, 1, 5, 1, 2, 5, 1, 5, 5, 4]))
    # 7
    print(Solution().minPairSum([3, 5, 2, 3]))
    # 8
    print(Solution().minPairSum([3, 5, 4, 2, 4, 6]))
