"""
 * 在二维网格 grid 上，有 4 种类型的方格：
 * 1、1 表示起始方格。且只有一个起始方格。
 * 2、2 表示结束方格，且只有一个结束方格。
 * 3、0 表示我们可以走过的空方格。
 * 4、-1 表示我们无法跨越的障碍。
 * 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
 * 每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
 * 提示：1 <= grid.length * grid[0].length <= 20
 * 链接：https://leetcode.cn/problems/unique-paths-iii/
"""
from typing import List


class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, vis):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1 or (r, c) in vis:
                return 0
            if grid[r][c] == 2:
                return 1 if len(vis) == m * n - 1 else 0

            vis.add((r, c))
            res = dfs(r - 1, c, vis) + dfs(r + 1, c, vis) + dfs(r, c - 1, vis) + dfs(r, c + 1, vis)
            vis.remove((r, c))
            return res

        vis = set()
        sx, sy = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                if grid[i][j] == -1:
                    vis.add((i, j))

        return dfs(sx, sy, vis)


if __name__ == '__main__':
    # 2
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
    # 4
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    # 0
    print(Solution().uniquePathsIII([[0, 1], [2, 0]]))
