"""
 * 给你一个长度为 n 的整数数组 nums。
 * 子数组 nums[l..r]（其中 0 <= l <= r < n）的 成本 定义为：
 * cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (-1)r - l
 * 你的任务是将 nums 分割成若干子数组，使得所有子数组的成本之和 最大化，并确保每个元素 正好 属于一个子数组。
 * 具体来说，如果 nums 被分割成 k 个子数组，且分割点为索引 i1, i2, ..., ik - 1（其中 0 <= i1 < i2 < ... < ik - 1 < n - 1），则总成本为：
 * cost(0, i1) + cost(i1 + 1, i2) + ... + cost(ik - 1 + 1, n - 1)
 * 返回在最优分割方式下的子数组成本之和的最大值。
 * 注意：如果 nums 没有被分割，即 k = 1，则总成本即为 cost(0, n - 1)。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/description/
"""
from functools import cache
from typing import List


class Solution:

    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(idx, f):
            if idx == n: return 0
            if f < 0:
                return dfs(idx + 1, 1) + nums[idx]
            return max(dfs(idx + 1, 1) + nums[idx], dfs(idx + 1, -1) - nums[idx])

        return dfs(0, -1)


if __name__ == '__main__':
    # 10
    print(Solution().maximumTotalCost([1, -2, 3, 4]))
    # 4
    print(Solution().maximumTotalCost([1, -1, 1, -1]))
    # 0
    print(Solution().maximumTotalCost([0]))
    # 2
    print(Solution().maximumTotalCost([1, -1]))
