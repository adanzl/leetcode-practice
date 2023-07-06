"""
 * 给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。
 * 一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。
 * 给你一个下标从 1 开始的二维数组 cells ，其中 cells[i] = [ri, ci] 表示在第 i 天，
 * 第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。
 * 你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。
 * 你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意 格子。你只能沿着 四个 基本方向移动（也就是上下左右）。
 * 请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。
 * 提示：
 * 1、2 <= row, col <= 2 * 10^4
 * 2、4 <= row * col <= 2 * 10^4
 * 3、cells.length == row * col
 * 4、1 <= ri <= row
 * 5、1 <= ci <= col
 * 6、cells 中的所有格子坐标都是 唯一 的。
 * 链接：https://leetcode.cn/problems/last-day-where-you-can-still-cross/
"""
from typing import List


class Solution:

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        parent = [i for i in range(row * col + 2)]
        mark = [[0] * col for _ in range(row)]
        for r, c in cells:
            mark[r - 1][c - 1] = 1

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(row):
            for j in range(col):
                if mark[i][j] == 1: continue
                for nx, ny in [(i, j + 1), (i + 1, j)]:
                    if 0 <= nx < row and 0 <= ny < col and mark[nx][ny] == 0:
                        r0, r1 = find(i * col + j), find(nx * col + ny)
                        parent[r1] = r0
                        if r1 != r0 and r0 < col and r1 >= col * (row - 1):
                            return n
        for i in range(len(cells) - 1, -1, -1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            mark[x][y] = 0
            for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if 0 <= nx < row and 0 <= ny < col and mark[nx][ny] == 0:
                    r0, r1 = find(x * col + y), find(nx * col + ny)
                    r_mn, r_mx = min(r0, r1), max(r0, r1)
                    if r_mn < col and r_mx >= col * (row - 1):
                        return i
                    if r_mn < col:
                        parent[r_mx] = r_mn
                    elif r_mx >= col * (row - 1):
                        parent[r_mn] = r_mx
                    else:
                        parent[r_mx] = r_mn
        return 0


if __name__ == '__main__':
    # 3
    print(Solution().latestDayToCross(6, col=2, cells=[[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2], [1, 2]]))
    # 2
    print(Solution().latestDayToCross(2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
    # 1
    print(Solution().latestDayToCross(2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))
    # 3
    print(Solution().latestDayToCross(3, col=3, cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
