"""
 * 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
 * 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
 * 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
 * 提示：
 * 1、1 <= nums.length <= 2500
 * 2、-10^4 <= nums[i] <= 10^4
 * 进阶：你能将算法的时间复杂度降低到 O(n log(n)) 吗?
 * 链接：https://leetcode.cn/problems/longest-increasing-subsequence/
"""

import bisect
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=20001
#
# [300] 最长递增子序列
#


# @lc code=start
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []  # g 下标表示长度，值表示最小的尾元素，g 是一个递增的数组
        for num in nums:
            # 如果最长递增要求是严格递增的，则修改为bisect_right
            idx = bisect.bisect_left(g, num)
            if idx == len(g):
                g.append(num)
            else:
                g[idx] = num
        return len(g)


# @lc code=end

#

if __name__ == '__main__':
    # 4
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # 4
    print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
    # 1
    print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
