"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 你可以执行任意次操作。
 * 每次操作中，你需要选择一个 子数组 ，并将这个子数组用它所包含元素的 和 替换。
 * 比方说，给定数组是 [1,3,5,6] ，你可以选择子数组 [3,5] ，用子数组的和 8 替换掉子数组，然后数组会变为 [1,8,6] 。
 * 请你返回执行任意次操作以后，可以得到的 最长非递减 数组的长度。
 * 子数组 指的是一个数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/find-maximum-non-decreasing-array-length
"""

from typing import List

#
# @lc app=leetcode.cn id=2945 lang=python3
#
# [2945] 找到最大非递减数组的长度
#


# @lc code=start
class Solution:

    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # 前 i 个元素，最长非递减序列长度
        last = [0] * (n + 1)  # 第 i 个元素，取dp[i] 时最大值的最小值
        # dp[i+1] >= dp[i]
        # 如果 sum([j+1...i]) >= last[j]，则 j 可以扩展到 i: pre_sum[i+1]-pre_sum[j+1]
        #   dp[i] = max(dp[i], dp[j] + 1)
        # last[i]越小，对结果越有利
        # 满足 s[i] >= s[j] + last[j] 的前提下，j越大，s[j]就越大，所以last[j]就越小，为了获得更大的j，要弹出队首
        # 转移之后，队列的后半部分，不一定满足 s[j] + last[j] <= s[i] + last[i]，为了保证队列的单调性，需要弹出队尾之后再将i入队
        q = [0]
        pre_sum = [0]
        for i, num in enumerate(nums):
            pre_sum.append(pre_sum[-1] + num)
            # 1. 去掉队首无用数据（计算转移时，直接取队首）
            while len(q) > 1 and pre_sum[q[1]] + last[q[1]] <= pre_sum[i + 1]:
                q.pop(0)
            # 2. 计算转移
            dp[i + 1] = dp[q[0]] + 1
            last[i + 1] = pre_sum[i + 1] - pre_sum[q[0]]
            # 3. 去掉队尾无用数据
            while q and pre_sum[q[-1]] + last[q[-1]] >= pre_sum[i + 1] + last[i + 1]:
                q.pop()
            q.append(i + 1)

        return dp[-1]


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().findMaximumLength([336, 78, 256, 976, 976, 764, 370, 46]))
    # 4
    print(Solution().findMaximumLength([1, 2, 3, 4]))
    # 3
    print(Solution().findMaximumLength([4, 3, 2, 6]))
