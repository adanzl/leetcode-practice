"""
 * 3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，
 * 其中每行、每列以及两条对角线上的各数之和都相等。
 * 给定一个由整数组成的row x col 的 grid，其中有多少个 3 x 3 的 “幻方” 子矩阵？
 * （每个子矩阵都是连续的）。
 * 注意：虽然幻方只能包含 1 到 9 的数字，但 grid 可以包含最多15的数字。
 * 提示:
 * 1、row == grid.length
 * 2、col == grid[i].length
 * 3、1 <= row, col <= 10
 * 4、0 <= grid[i][j] <= 15
 * 链接：https://leetcode.cn/problems/magic-squares-in-grid/
"""

from typing import List

#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#


# @lc code=start
class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        # 3 阶幻方只有8种
        l = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [2, 7, 6, 9, 5, 1, 4, 3, 8],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
        ]
        for i in range(m - 2):
            for j in range(n - 2):
                temp = grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]
                if temp in l:
                    ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
    # 0
    print(Solution().numMagicSquaresInside([[8]]))
