"""
 * 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。
 * 当你在格子 (i, j) 的时候，你可以移动到以下格子之一：
 * 1、满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
 * 2、满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
 * 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 10^5
 * 5、0 <= grid[i][j] < m * n
 * 6、grid[m - 1][n - 1] == 0
 * 链接：https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/
"""
from typing import Deque, List

from sortedcontainers import SortedList


class Solution:

    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [SortedList([i for i in range(1, n)]) for _ in range(m)]
        cols = [SortedList([i for i in range(1, m)]) for _ in range(n)]
        ans = [[-1] * n for _ in range(m)]
        ans[0][0] = 1
        q = Deque([[0, 0]])
        d = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                rr, cc = rows[x], cols[y]
                rr.discard(y)
                cc.discard(x)
                if ans[x][y] == -1: ans[x][y] = d
                v = grid[x][y]
                idx = rr.bisect_left(y)
                while idx != len(rr):
                    ny = int(rr[idx])  # type: ignore
                    if ny > y + v:
                        break
                    if ans[x][ny] == -1:
                        q.append([x, ny])
                    rr.remove(ny)
                idx = cc.bisect_left(x)
                while idx != len(cc):
                    nx = int(cc[idx])  # type: ignore
                    if nx > x + v:
                        break
                    if ans[nx][y] == -1:
                        q.append([nx, y])
                    cc.remove(nx)
                # for ny in rr.irange(y, y + v):  此处用irange会超时
                #     if ans[x][ny] == -1: q.append((x, ny))
                # for nx in cc.irange(x, x + v):
                #     if ans[nx][y] == -1: q.append((nx, y))
            d += 1
        return ans[-1][-1]


if __name__ == '__main__':
    # 3
    print(Solution().minimumVisitedCells([[7, 12, 11, 11, 4], [10, 5, 16, 15, 7], [7, 9, 6, 16, 7], [1, 13, 3, 16, 0]]))
    # 3
    print(Solution().minimumVisitedCells([[3, 2], [0, 0]]))
    # 4
    print(Solution().minimumVisitedCells([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]))
    # 3
    print(Solution().minimumVisitedCells([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]))
    # -1
    print(Solution().minimumVisitedCells([[2, 1, 0], [1, 0, 0]]))
