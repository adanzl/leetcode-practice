"""
 * 给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。
 * 在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
 * 返回 最大非负积 对 10^9 + 7 取余 的结果。如果最大积为负数，则返回 -1 。
 * 注意，取余是在得到最大积之后执行的。
 * 提示：
 * 1、1 <= rows, cols <= 15
 * 2、-4 <= grid[i][j] <= 4
 * 链接：https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/
"""
from typing import List


class Solution:

    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        row, col = len(grid), len(grid[0])
        dp = [[list([0, -1, 0]) for _ in range(col + 1)] for __ in range(row + 1)]  # - 0 +
        dp[1][0] = [0, -1, 1]
        for r in range(row):
            for c in range(col):
                v = grid[r][c]
                if v == 0:
                    dp[r + 1][c + 1] = [0, 0, 0]
                elif v > 0:
                    dp[r + 1][c + 1][0] = min(dp[r + 1][c][0] * v, dp[r][c + 1][0] * v)
                    dp[r + 1][c + 1][1] = 0 if dp[r + 1][c][1] != -1 or dp[r][c + 1][1] != -1 else -1
                    dp[r + 1][c + 1][2] = max(dp[r + 1][c][2] * v, dp[r][c + 1][2] * v)
                else:
                    dp[r + 1][c + 1][0] = min(dp[r + 1][c][2] * v, dp[r][c + 1][2] * v)
                    dp[r + 1][c + 1][1] = 0 if dp[r + 1][c][1] != -1 or dp[r][c + 1][1] != -1 else -1
                    dp[r + 1][c + 1][2] = max(dp[r + 1][c][0] * v, dp[r][c + 1][0] * v)
        if dp[-1][-1][2]: return dp[-1][-1][2] % MOD
        if dp[-1][-1][1] != -1: return 0
        return -1


if __name__ == '__main__':
    # 8
    print(Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
    # -1
    print(Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
    # 0
    print(Solution().maxProductPath([[1, 3], [0, -4]]))
    # 2
    print(Solution().maxProductPath([[1, 4, 4, 0], [-2, 0, 0, 1], [1, -1, 1, 1]]))
