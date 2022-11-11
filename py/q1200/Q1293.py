"""
 * 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
 * 如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。
 * 提示：
 * 1、grid.length == m
 * 2、grid[0].length == n
 * 3、1 <= m, n <= 40
 * 4、1 <= k <= m*n
 * 5、grid[i][j] 是 0 或 1
 * 6、grid[0][0] == grid[m-1][n-1] == 0
 * 链接：https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
from typing import Deque, List


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 0
        k = min(k, m + n - 3)
        vis = set()
        q = Deque()
        q.append((0, 0, k))
        vis.add((0, 0, k))
        dis = 0
        while q:
            dis += 1
            size = len(q)
            while size:
                x, y, r = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1: continue
                    if (nx, ny, r) in vis: continue
                    vis.add((nx, ny, r))
                    nk = (r - 1) if grid[nx][ny] else r
                    if nk >= 0:
                        q.append((nx, ny, nk))
                        if nx == m - 1 and ny == n - 1: return dis
                size -= 1
        return -1


if __name__ == '__main__':
    # 14
    print(Solution().shortestPath([[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 0], [0, 0]], 4))
    # 6
    print(Solution().shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1))
    # -1
    print(Solution().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1))
