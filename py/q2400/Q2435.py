"""
 * 给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点 (m - 1, n - 1) 。
 * 请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 5 * 10^4
 * 4、1 <= m * n <= 5 * 10^4
 * 5、0 <= grid[i][j] <= 100
 * 6、1 <= k <= 50
 * 链接：https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
"""
from typing import List


class Solution:

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])  # row m, column n
        dp = [[[0] * (n) for _ in range(m)] for i in range(k)]
        dp[grid[0][0] % k][0][0] = 1
        for i in range(1, n):
            for r in range(k):
                dp[(grid[0][i] + r) % k][0][i] += dp[r][0][i - 1]
        for i in range(1, m):
            for r in range(k):
                dp[(grid[i][0] + r) % k][i][0] += dp[r][i - 1][0]
            for j in range(1, n):
                for r in range(k):
                    key = (r + grid[i][j]) % k
                    dp[key][i][j] += dp[r][i][j - 1] + dp[r][i - 1][j]
                    dp[key][i][j] %= MOD
        return dp[0][-1][-1] % MOD


if __name__ == '__main__':
    # 2
    print(Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3))
    # 1
    print(Solution().numberOfPaths([[0, 0]], 5))
    # 10
    print(Solution().numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1))
