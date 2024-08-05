"""
 * 交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
 * 环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
 * 给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums[i] 为 0 或者 1
 * 链接：https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/
"""

from typing import List

#
# @lc app=leetcode.cn id=2134 lang=python3
#
# [2134] 最少交换次数来组合所有的 1 II
#


# @lc code=start
class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        ans = len(nums)
        size_1 = sum(nums)
        if size_1 == 0: return 0
        pre_cnt0 = [0]
        for i, num in enumerate(nums + nums):
            if num == 0:
                pre_cnt0.append(pre_cnt0[-1] + 1)
            else:
                pre_cnt0.append(pre_cnt0[-1])

        for i, num in enumerate(nums):
            if num == 1:
                ii_r = i + size_1
                ans = min(ans, pre_cnt0[ii_r] - pre_cnt0[i])
        return max(ans, 0)


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().minSwaps([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]))
    # 0
    print(Solution().minSwaps([0, 0, 0]))
    # 1
    print(Solution().minSwaps([0, 1, 0, 1, 1, 0, 0]))
    # 2
    print(Solution().minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))
    # 0
    print(Solution().minSwaps([1, 1, 0, 0, 1]))
