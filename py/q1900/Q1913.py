"""
 * 两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
 * 例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
 * 给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。
 * 返回以这种方式取得的乘积差中的 最大值 。
 * 提示：
 * 1、4 <= nums.length <= 10^4
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-product-difference-between-two-pairs
"""

from typing import List

#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#


# @lc code=start
class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


# @lc code=end

if __name__ == '__main__':
    # 34
    print(Solution().maxProductDifference([5, 6, 2, 7, 4]))
    # 64
    print(Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]))
