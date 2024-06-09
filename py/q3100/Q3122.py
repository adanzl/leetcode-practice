"""
 * 给你一个大小为 m x n 的二维矩形 grid 。每次 操作 中，你可以将 任一 格子的值修改为 任意 非负整数。
 * 完成所有操作后，你需要确保每个格子 grid[i][j] 的值满足：
 * 1、如果下面相邻格子存在的话，它们的值相等，也就是 grid[i][j] == grid[i + 1][j]（如果存在）。
 * 2、如果右边相邻格子存在的话，它们的值不相等，也就是 grid[i][j] != grid[i][j + 1]（如果存在）。
 * 请你返回需要的 最少 操作数目。
 * 提示：
 * 1、1 <= n, m <= 1000
 * 2、0 <= grid[i][j] <= 9
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-satisfy-conditions/
"""
from typing import Counter, List


class Solution:

    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        LIMIT = 0x3c3c3c3c3c3c3c
        dp = [[LIMIT for _ in range(10)] for _ in range(n)]
        cnt = [Counter() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                cnt[j][grid[i][j]] += 1
        for i in range(10):
            dp[0][i] = sum(cnt[0].values()) - cnt[0][i]
        for i in range(1, n):
            for j in range(10):
                val = sum(cnt[i].values()) - cnt[i][j]
                for k in range(10):
                    if j == k: continue
                    dp[i][j] = min(dp[i][j], val + dp[i - 1][k])
        return min(dp[-1])


if __name__ == '__main__':
    # 0
    print(Solution().minimumOperations([[1, 0, 2], [1, 0, 2]]))
    # 3
    print(Solution().minimumOperations([[1, 1, 1], [0, 0, 0]]))
    # 2
    print(Solution().minimumOperations([[1], [2], [3]]))
