"""
 * 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
 * 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
 * 返回分配方案中尽可能 最小 的 最大工作时间 。
 * 提示：
 * 1、1 <= k <= jobs.length <= 12
 * 2、1 <= jobs[i] <= 10^7
 * 链接：https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs/
"""
from typing import List
from functools import cache

subsets = [[] for _ in range(1 << 12)]
for i in range(1 << 12):
    s = i
    while s:
        subsets[i].append(s)
        s = (s - 1) & i


class Solution:

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 数位dp 这个解法在 美服 过不了
        n = len(jobs)
        # 预处理每种状态的开销
        sm = [0] * (1 << n)
        for i in range(1, 1 << n):
            low_bit = i & -i
            sm[i] += sm[i - low_bit] + jobs[low_bit.bit_length() - 1]
        # dp[i][j] 前i个人，完成状态j的工作分配的做小开销
        # 转移方程 dp[i][j] 第i个人完成了状态s，其他人完成了状态j-s，枚举s，取最小值
        # dp = [[0] * (1 << n) for _ in range(k)]
        dp = sm.copy()

        for i in range(1, k):
            for j in range((1 << n) - 1, 0, -1):
                for s in subsets[j]:  # 遍历二进制子集
                    v = dp[j ^ s]
                    if sm[s] > v: v = sm[s]  # 不要用 max 和 min，那样会有额外的函数调用开销
                    if v < dp[j]: dp[j] = v
        return dp[-1]


if __name__ == '__main__':
    # 11
    print(Solution().minimumTimeRequired([1, 2, 4, 7, 8], k=2))
    # 3
    print(Solution().minimumTimeRequired([3, 2, 3], k=3))
    # 9899456
    print(Solution().minimumTimeRequired([
        9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365,
        3758448, 9881935, 2420271, 4542202
    ], 9))
