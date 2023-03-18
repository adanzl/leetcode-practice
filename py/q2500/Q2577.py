"""
 * 给你一个 m x n 的矩阵 grid ，每个元素都为 非负 整数，其中 grid[row][col] 表示可以访问格子 (row, col) 的 最早 时间。
 * 也就是说当你访问格子 (row, col) 时，最少已经经过的时间为 grid[row][col] 。
 * 你从 最左上角 出发，出发时刻为 0 ，你必须一直移动到上下左右相邻四个格子中的 任意 一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。
 * 请你返回 最早 到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 -1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、2 <= m, n <= 1000
 * 4、4 <= m * n <= 10^5
 * 5、0 <= grid[i][j] <= 10^5
 * 6、grid[0][0] == 0
 * 链接：https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        n, m = len(grid), len(grid[0])
        dis = [[float('inf')] * m for _ in range(n)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            d, x, y = heappop(h)
            if x == n - 1 and y == m - 1:
                return d
            for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if 0 <= nx < n and 0 <= ny < m:
                    nd = max(d + 1, grid[nx][ny])
                    nd += (nd - nx - ny) % 2  # nd 必须和 x+y 同奇偶
                    if nd < dis[nx][ny]:
                        dis[nx][ny] = nd
                        heappush(h, (nd, nx, ny))
        return -1


if __name__ == '__main__':
    # 7
    print(Solution().minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]))
    # -1
    print(Solution().minimumTime([[0, 2, 4], [3, 2, 1], [1, 0, 4]]))
