"""
 * 给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。
 * 你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。
 * 从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。
 * 你可以从 任一 单元格开始，并且必须至少移动一次。
 * 返回你能得到的 最大 总得分。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、2 <= m, n <= 1000
 * 4、4 <= m * n <= 10^5
 * 5、1 <= grid[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-difference-score-in-a-grid/description/
"""
from typing import List


class Solution:

    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 0x3c3c3c3c3c3c
        ans = -INF
        col, row = [INF] * n, [INF] * m
        for i in range(m):
            row[i] = min(row[i], grid[i][0])
            if i > 0:
                ans = max(ans, grid[i][0] - row[i - 1])
                row[i] = min(row[i], row[i - 1])
        for i in range(n):
            col[i] = min(col[i], grid[0][i])
            if i > 0: 
                ans = max(ans, grid[0][i] - col[i - 1])
                col[i] = min(col[i], col[i - 1])
        for i in range(1, m):
            for j in range(1, n):
                v_col = grid[i][j] - col[j]
                v_row = grid[i][j] - row[i]
                ans = max(ans, v_col, v_row)
                col[j] = min(col[j], grid[i][j], row[i])
                row[i] = min(row[i], grid[i][j], col[j])
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().maxScore([[4, 9], [5, 2], [3, 1]]))
    # 9
    print(Solution().maxScore([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]))
    # -1
    print(Solution().maxScore([[4, 3, 2], [3, 2, 1]]))
