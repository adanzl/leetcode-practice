"""
 * 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
 * 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
 * 在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
 * 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
 * 提示：
 * 1、n == matrix.length == matrix[i].length
 * 2、1 <= n <= 100
 * 3、-100 <= matrix[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
"""
from typing import List


class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        for line in matrix:
            ndp = [0] * n
            for i, v in enumerate(line):
                v = dp[i]
                if i > 0: v = min(v, dp[i - 1])
                if i < n - 1: v = min(v, dp[i + 1])
                ndp[i] = v + line[i]
            dp = ndp
        return min(dp)


if __name__ == '__main__':
    # 13
    print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    # -59
    print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))