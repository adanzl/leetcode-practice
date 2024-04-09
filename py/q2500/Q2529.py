"""
 * 给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
 * 换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
 * 注意：0 既不是正整数也不是负整数。
 * 提示：
 * 1、1 <= nums.length <= 2000
 * 2、-2000 <= nums[i] <= 2000
 * 3、nums 按 非递减顺序 排列。
 * 链接：https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer
"""

from typing import List

#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#


# @lc code=start
class Solution:

    def maximumCount(self, nums: List[int]) -> int:
        c_n, c_p = 0, 0
        for num in nums:
            if num > 0:
                c_p += 1
            elif num < 0:
                c_n += 1
        return max(c_n, c_p)


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().maximumCount([-2, -1, -1, 1, 2, 3]))
    # 3
    print(Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]))
    # 4
    print(Solution().maximumCount([5, 20, 66, 1314]))
