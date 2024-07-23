"""
 * 给你一个二维字符矩阵 grid，其中 grid[i][j] 可能是 'X'、'Y' 或 '.'，返回满足以下条件的 子矩阵 数量：
 * 1、包含 grid[0][0]
 * 2、'X' 和 'Y' 的频数相等。
 * 3、至少包含一个 'X'。
 * 提示：
 * 1、1 <= grid.length, grid[i].length <= 1000
 * 2、grid[i][j] 可能是 'X'、'Y' 或 '.'.
 * 链接：https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/
"""
from typing import List


class Solution:

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        pre_sum_x = [[0] * (n + 1) for _ in range(m + 1)]
        pre_sum_y = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                vx, vy = 0, 0
                if grid[i][j] == 'X':
                    vx = 1
                elif grid[i][j] == 'Y':
                    vy = 1
                pre_sum_x[i + 1][j + 1] = pre_sum_x[i + 1][j] + pre_sum_x[i][j + 1] - pre_sum_x[i][j] + vx
                pre_sum_y[i + 1][j + 1] = pre_sum_y[i + 1][j] + pre_sum_y[i][j + 1] - pre_sum_y[i][j] + vy
                if pre_sum_x[i + 1][j + 1] == pre_sum_y[i + 1][j + 1] and pre_sum_y[i + 1][j + 1]:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
    # 0
    print(Solution().numberOfSubmatrices([["X", "X"], ["X", "Y"]]))
    # 0
    print(Solution().numberOfSubmatrices([[".", "."], [".", "."]]))
