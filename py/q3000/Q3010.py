"""
 * 给你一个长度为 n 的整数数组 nums 。
 * 一个数组的 代价 是它的 第一个 元素。比方说，[1,2,3] 的代价是 1 ，[3,4,1] 的代价是 3 。
 * 你需要将 nums 分成 3 个 连续且没有交集 的子数组。
 * 请你返回这些子数组的 最小 代价 总和 。
 * 提示：
 * 1、3 <= n <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
"""
from typing import List


class Solution:

    def minimumCost(self, nums: List[int]) -> int:
        ss = sorted(nums[1:])
        return nums[0] + ss[0] + ss[1]


if __name__ == '__main__':
    # 6
    print(Solution().minimumCost([1, 2, 3, 12]))
    # 12
    print(Solution().minimumCost([5, 4, 3]))
    # 12
    print(Solution().minimumCost([10, 3, 1, 1]))
