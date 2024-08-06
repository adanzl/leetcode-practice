"""
 * 给你一个整数数组 nums 和两个整数 cost1 和 cost2 。你可以执行以下 任一 操作 任意 次：
 * 1、从 nums 中选择下标 i 并且将 nums[i] 增加 1 ，开销为 cost1。
 * 2、选择 nums 中两个 不同 下标 i 和 j ，并且将 nums[i] 和 nums[j] 都 增加 1 ，开销为 cost2 。
 * 你的目标是使数组中所有元素都 相等 ，请你返回需要的 最小开销 之和。
 * 由于答案可能会很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 3、1 <= cost1 <= 10^6
 * 4、1 <= cost2 <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-cost-to-equalize-array/
"""

from typing import List

#
# @lc app=leetcode.cn id=3139 lang=python3
#
# [3139] 使数组中所有元素相等的最小开销
#


# @lc code=start
class Solution:

    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        MX, ans = max(nums), 0x3c3c3c3c3c3c3c3c
        if cost2 >= 2 * cost1:  # 这说明操作2毫无意义
            return (n * MX - sum(nums)) * cost1 % MOD
        # n 个数nums，一次取两个(成本cost2)或者取一个(成本cost1)减1，求最少成本
        # mxValue表示最大值，sm=sum(nums), h_sm = sm // 2
        # 如果 mxValue >= h_sm，val = cost1*(mxValue - (sm-mxValue)) + cost2*(sm-mxValue)
        # 如果 mxValue < h_sm，val = cost2*h_sm + cost1*(sm&1)
        min = lambda x, y: x if x < y else y
        sm_diff, max_diff = 0, 0
        for d in [MX - num for num in nums]:
            sm_diff += d
            max_diff = max(max_diff, d)
        for t_offset in range(MX + 1):
            sm = sm_diff + t_offset * n
            h_sm = sm >> 1
            mxValue = max_diff + t_offset
            if mxValue > h_sm:
                ans = min(ans, cost1 * (mxValue * 2 - sm) + cost2 * (sm - mxValue))
            else:
                ans = min(ans, cost2 * h_sm + cost1 * (sm & 1))
        return ans % MOD


# @lc code=end

if __name__ == '__main__':
    #
    print(Solution().minCostToEqualizeArray([8, 6, 1000000, 5], 1000000, 1))
    # 21
    print(Solution().minCostToEqualizeArray([7, 4, 8], 7, 3))
    # 8
    print(Solution().minCostToEqualizeArray([4, 3, 1, 8], 5, 1))
    # 15
    print(Solution().minCostToEqualizeArray([4, 1], cost1=5, cost2=2))
    # 6
    print(Solution().minCostToEqualizeArray([2, 3, 3, 3, 5], cost1=2, cost2=1))
    # 4
    print(Solution().minCostToEqualizeArray([3, 5, 3], cost1=1, cost2=3))
