"""
 * 你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。
 * 你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。
 * 给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。
 * 返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。
 * 提示：
 * 1、1 <= jobDifficulty.length <= 300
 * 2、0 <= jobDifficulty[i] <= 1000
 * 3、1 <= d <= 10
 * 链接：https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/
"""
from functools import cache
from typing import List


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: return -1
        min = lambda a, b: a if a < b else b
        @cache
        def max_d(l, r):
            return max(jobDifficulty[l:r])
        # dp[i][j] works-days max
        dp = [[0x3c3c3c3c] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):  # works
            for j in range(1, d + 1):  # days
                for l in range(1, i - (j - 1) + 1):  # 最后一天干多少任务
                    dp[i][j] = min(dp[i][j], dp[i - l][j - 1] + max_d(i-l, i))
        return dp[n][d]


if __name__ == '__main__':
    # 7
    print(Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2))
    # -1
    print(Solution().minDifficulty([9, 9, 9], 4))
    # 3
    print(Solution().minDifficulty([1, 1, 1], 3))
    # 15
    print(Solution().minDifficulty([7, 1, 7, 1, 7, 1], 3))
    # 843
    print(Solution().minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))
