"""
 * 给你一个 m x n 的二进制矩形 grid 和一个整数 health 表示你的健康值。
 * 你开始于矩形的左上角 (0, 0) ，你的目标是矩形的右下角 (m - 1, n - 1) 。
 * 你可以在矩形中往上下左右相邻格子移动，但前提是你的健康值始终是 正数 。
 * 对于格子 (i, j) ，如果 grid[i][j] = 1 ，那么这个格子视为 不安全 的，会使你的健康值减少 1 。
 * 如果你可以到达最终的格子，请你返回 true ，否则返回 false 。
 * 注意 ，当你在最终格子的时候，你的健康值也必须为 正数 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 50
 * 4、2 <= m * n
 * 5、1 <= health <= m + n
 * 6、grid[i][j] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        ans = [[INF] * n for _ in range(m)]
        ans[0][0] = grid[0][0]
        q = [[0, 0]]
        
        while q:
            x, y = q.pop(0)
            for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ans[x][y] + grid[nx][ny] < ans[nx][ny]:
                    ans[nx][ny] = ans[x][y] + grid[nx][ny]
                    q.append([nx, ny])
        return ans[m - 1][n - 1] < health


if __name__ == '__main__':
    # False
    print(Solution().findSafeWalk([[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]],
                                  health=3))
    # True
    print(Solution().findSafeWalk([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1))
    # True
    print(Solution().findSafeWalk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5))
