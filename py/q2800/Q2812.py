"""
 * 给你一个下标从 0 开始、大小为 n x n 的二维矩阵 grid ，其中 (r, c) 表示：
 * 1、如果 grid[r][c] = 1 ，则表示一个存在小偷的单元格
 * 2、如果 grid[r][c] = 0 ，则表示一个空单元格
 * 你最开始位于单元格 (0, 0) 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。
 * 矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。
 * 返回所有通向单元格 (n - 1, n - 1) 的路径中的 最大安全系数 。
 * 单元格 (r, c) 的某个 相邻 单元格，是指在矩阵中存在的 (r, c + 1)、(r, c - 1)、(r + 1, c) 和 (r - 1, c) 之一。
 * 两个单元格 (a, b) 和 (x, y) 之间的 曼哈顿距离 等于 | a - x | + | b - y | ，其中 |val| 表示 val 的绝对值。
 * 提示：
 * 1、1 <= grid.length == n <= 400
 * 2、grid[i].length == n
 * 3、grid[i][j] 为 0 或 1
 * 4、grid 至少存在一个小偷
 * 链接：https://leetcode.cn/problems/find-the-safest-path-in-a-grid/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def maximumSafenessFactor1(self, grid: List[List[int]]) -> int:
        # dijkstra 解法，在国服会超时，在美服可以AC，java版本可以AC
        n = len(grid)
        md = [[-1] * n for _ in range(n)]

        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    md[i][j] = 0
        for d in range(n * n):
            for _ in range(len(q)):
                i, j = q.pop(0)
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= x < n and 0 <= y < n and md[x][y] == -1:
                        md[x][y] = d + 1
                        q.append((x, y))
            if not q:
                break
        vis = [[False] * n for _ in range(n)]
        dist = [[-1] * n for _ in range(n)]
        dist[0][0] = md[0][0]
        q = [[-md[0][0], 0, 0]]  # cost-x-y
        while q:
            mx, i, j = heappop(q)
            if vis[i][j]: continue
            for nx, ny in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= nx < n and 0 <= ny < n:
                    nv = min(md[nx][ny], -mx)
                    if nv > dist[nx][ny]:
                        dist[nx][ny] = nv
                        heappush(q, [-nv, nx, ny])
            vis[i][j] = True
        return dist[-1][-1]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # 并查集解法
        n = len(grid)
        q = []
        dis = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0

        groups = [q]
        while q:  # 多源 BFS
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] < 0:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)  # 相同 dis 分组记录

        # 并查集模板
        fa = list(range(n * n))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        fa[find(x * n + y)] = find(i * n + j)
            if find(0) == find(n * n - 1):  # 写这里判断更快些
                return d
        return 0


if __name__ == '__main__':
    # 0
    print(Solution().maximumSafenessFactor([[1]]))
    # 2
    print(Solution().maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
    # 0
    print(Solution().maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
    # 2
    print(Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
