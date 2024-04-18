"""
 * 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
 * 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。
 * 整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
 * 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
 * 格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。
 * 计算这个岛屿的周长。
 * 提示：
 * 1、row == grid.length
 * 2、col == grid[i].length
 * 3、1 <= row, col <= 100
 * 4、grid[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/island-perimeter/
"""

from typing import List

#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#


# @lc code=start
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                ans += 1 if i == 0 or grid[i - 1][j] == 0 else 0  # up
                ans += 1 if i == m - 1 or grid[i + 1][j] == 0 else 0  # down
                ans += 1 if j == 0 or grid[i][j - 1] == 0 else 0  # left
                ans += 1 if j == n - 1 or grid[i][j + 1] == 0 else 0  # right
        return ans


# @lc code=end

if __name__ == '__main__':
    # 16
    print(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
    # 4
    print(Solution().islandPerimeter([[1]]))
    # 4
    print(Solution().islandPerimeter([[1, 0]]))
