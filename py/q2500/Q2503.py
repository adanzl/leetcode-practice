"""
 * 给你一个大小为 m x n 的整数矩阵 grid 和一个大小为 k 的数组 queries 。
 * 找出一个大小为 k 的数组 answer ，且满足对于每个整数 queries[i] ，你从矩阵 左上角 单元格开始，重复以下过程：
 * 1、如果 queries[i] 严格 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 4 个方向（上、下、左、右）上任一 相邻 单元格。
 * 2、否则，你不能获得任何分，并且结束这一过程。
 * 在过程结束后，answer[i] 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 多次 。
 * 返回结果数组 answer 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、2 <= m, n <= 1000
 * 4、4 <= m * n <= 10^5
 * 5、k == queries.length
 * 6、1 <= k <= 10^4
 * 7、1 <= grid[i][j], queries[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/
"""
from heapq import heappop, heappush
from typing import Deque, List


class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # 离线
        m, n = len(grid), len(grid[0])
        nn = len(queries)  # 1e4
        h = [[grid[0][0], 0, 0]]  # val, x, y
        grid[0][0] = 0
        ans = [0] * nn
        pre = 0
        for idx, val in sorted(enumerate(queries), key=lambda x: x[1]):
            ans[idx] = pre
            while h and h[0][0] < val:
                _, x, y = heappop(h)
                ans[idx] += 1
                for dx, dy in [-1, 0], [0, -1], [1, 0], [0, 1]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1 or grid[nx][ny] == 0: continue
                    heappush(h, [grid[nx][ny], nx, ny])
                    grid[nx][ny] = 0
            pre = ans[idx]
        return ans

    def maxPoints2(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # 这个 bfs 美服 会超时
        m, n = len(grid), len(grid[0])
        nn = len(queries)
        ans = [0] * nn
        q = Deque([[0, 0]])
        vis = [[False] * n for _ in range(m)]
        pre = 0
        for idx, val in sorted(enumerate(queries), key=lambda x: x[1]):
            nxt = set()
            ans[idx] = pre
            while q:
                x, y = q.popleft()
                if grid[x][y] >= val:
                    nxt.add((x, y))
                    continue
                if vis[x][y]: continue
                vis[x][y] = True
                ans[idx] += 1
                for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1 or vis[nx][ny]: continue
                    q.append([nx, ny])
            pre = ans[idx]
            q = Deque(nxt)
        return ans


if __name__ == '__main__':
    # [5,8,1]
    print(Solution().maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]))
    # [0]
    print(Solution().maxPoints([[5, 2, 1], [1, 1, 2]], [3]))
    #
    # print(Solution().maxPoints())