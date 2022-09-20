"""
 * 给你两个长度分别 n 和 m 的整数数组 nums 和 multipliers ，其中 n >= m ，数组下标 从 1 开始 计数。
 * 初始时，你的分数为 0 。你需要执行恰好 m 步操作。在第 i 步操作（从 1 开始 计数）中，需要：
 * 1、选择数组 nums 开头处或者末尾处 的整数 x 。
 * 2、你获得 multipliers[i] * x 分，并累加到你的分数中。
 * 3、将 x 从数组 nums 中移除。
 * 在执行 m 步操作后，返回 最大 分数。
 * 提示：
 * 1、n == nums.length
 * 2、m == multipliers.length
 * 3、1 <= m <= 10^3
 * 4、m <= n <= 10^5
 * 5、-1000 <= nums[i], multipliers[i] <= 1000
 * 链接：https://leetcode.cn/problems/maximum-score-from-performing-multiplication-operations/
"""
from typing import *
from math import *
from collections import *


class Solution:

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + nums[i - 1] * multipliers[i - 1]
            dp[0][i] = dp[0][i - 1] + nums[n - i] * multipliers[i - 1]
        ans = dp[0][m]
        for i in range(1, m + 1):
            for j in range(1, m + 1 - i):
                v1 = multipliers[i + j - 1] * nums[i - 1] + dp[i - 1][j]
                v2 = multipliers[i + j - 1] * nums[n - j] + dp[i][j - 1]
                dp[i][j] = v1 if v1 > v2 else v2
            ans = dp[i][m - i] if dp[i][m - i] > ans else ans
        return ans




if __name__ == '__main__':
    # 14
    print(Solution().maximumScore([1, 2, 3], [3, 2, 1]))
    # 102
    print(Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
