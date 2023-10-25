"""
 * 有一个 矩形网格 状的农场，划分为 m 行 n 列的单元格。每个格子要么是 肥沃的 （用 1 表示），要么是 贫瘠 的（用 0 表示）。
 * 网格图以外的所有与格子都视为贫瘠的。
 * 农场中的 金字塔 区域定义如下：
 * 1、区域内格子数目 大于 1 且所有格子都是 肥沃的 。
 * 2、金字塔 顶端 是这个金字塔 最上方 的格子。金字塔的高度是它所覆盖的行数。
 *    令 (r, c) 为金字塔的顶端且高度为 h ，那么金字塔区域内包含的任一格子 (i, j) 需满足 r <= i <= r + h - 1 且 c - (i - r) <= j <= c + (i - r) 。
 * 一个 倒金字塔 类似定义如下：
 * 1、区域内格子数目 大于 1 且所有格子都是 肥沃的 。
 * 2、倒金字塔的 顶端 是这个倒金字塔 最下方 的格子。倒金字塔的高度是它所覆盖的行数。
 *    令 (r, c) 为金字塔的顶端且高度为 h ，那么金字塔区域内包含的任一格子 (i, j) 需满足 r - h + 1 <= i <= r 且 c - (r - i) <= j <= c + (r - i) 。
 * 下图展示了部分符合定义和不符合定义的金字塔区域。黑色区域表示肥沃的格子。
 * 给你一个下标从 0 开始且大小为 m x n 的二进制矩阵 grid ，它表示农场，请你返回 grid 中金字塔和倒金字塔的 总数目 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 1000
 * 4、1 <= m * n <= 10^5
 * 5、grid[i][j] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
"""

from itertools import accumulate
from typing import List

#
# @lc app=leetcode.cn id=2088 lang=python3
#
# [2088] 统计农场中肥沃金字塔的数目
#


# @lc code=start
class Solution:

    def countPyramids(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp_u[i][j] 表示以grid[i][j]为顶的金字塔的高度 dp_dp[i][j] 反之
        dp_u = [[grid[i][j] for j in range(n)] for i in range(m)]
        dp_d = [[grid[i][j] for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(m - 2, -1, -1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dp_u[i][j] = 0
                else:
                    dp_u[i][j] = min(dp_u[i + 1][j - 1], dp_u[i + 1][j], dp_u[i + 1][j + 1]) + 1
                    ans += dp_u[i][j] - 1
        for i in range(1, m):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dp_d[i][j] = 0
                else:
                    dp_d[i][j] = min(dp_d[i - 1][j - 1], dp_d[i - 1][j], dp_d[i - 1][j + 1]) + 1
                    ans += dp_d[i][j] - 1
        return ans

    def countPyramids1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        p_sum = [[0] + list(accumulate(grid[i])) for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                for d in range(1, m - i):
                    l, r = j - d, j + d
                    if l < 0 or r > n - 1: break
                    ss = p_sum[i + d][r + 1] - p_sum[i + d][l]
                    if ss != d * 2 + 1: break
                    ans += 1
                for d in range(1, i + 1):
                    l, r = j - d, j + d
                    if l < 0 or r > n - 1: break
                    ss = p_sum[i - d][r + 1] - p_sum[i - d][l]
                    if ss != d * 2 + 1: break
                    ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 13
    print(Solution().countPyramids([[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 0, 1]]))
    # 2
    print(Solution().countPyramids([[0, 1, 1, 0], [1, 1, 1, 1]]))
    # 2
    print(Solution().countPyramids([[1, 1, 1], [1, 1, 1]]))
    # 0
    print(Solution().countPyramids([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
