"""
 * 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
 * 返回执行此操作后，grid 中最大的岛屿面积是多少？
 * 岛屿 由一组上、下、左、右四个方向相连的 1 形成。
 * 提示：
 * 1、n == grid.length
 * 2、n == grid[i].length
 * 3、1 <= n <= 500
 * 4、grid[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/making-a-large-island/
"""
from typing import List


class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))
        areas = [0] * n * m
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def find(x):
            nonlocal parent
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        def merge(v1, v2):
            r1, r2 = find(v1), find(v2)
            if r1 == r2: return
            nonlocal parent
            parent[r2] = r1
            areas[r1] += areas[r2]

        for i in range(m):
            for j in range(n):
                areas[i * n + j] = grid[i][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                for d in dirs:
                    nx, ny = i + d[0], j + d[1]
                    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1 or grid[nx][ny] == 0: continue
                    merge(i * n + j, nx * n + ny)
        ans = max(areas)
        if ans == 0: return 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: continue
                area = set()
                for d in dirs:
                    nx, ny = i + d[0], j + d[1]
                    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1: continue
                    area.add(find(nx * n + ny))
                ans = max(ans, sum(areas[i] for i in area) + 1)
        return ans


if __name__ == '__main__':
    # 18
    print(Solution().largestIsland([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0]]))
    # 2
    print(Solution().largestIsland([[0, 0], [0, 1]]))
    # 4
    print(Solution().largestIsland([[1, 1], [1, 0]]))
    # 3
    print(Solution().largestIsland([[1, 0], [0, 1]]))
    # 4
    print(Solution().largestIsland([[1, 1], [1, 1]]))