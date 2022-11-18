"""
 * 给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：
 * 1、下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
 * 2、下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
 * 3、下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
 * 4、下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
 * 注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。
 * 一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，最
 * 终在最右下角的格子 (m - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。
 * 你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。
 * 请你返回让网格图至少有一条有效路径的最小代价。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 100
 * 链接：https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
"""
from typing import List
from heapq import heappop, heappush

######################## Template ########################
INF = int(1e18)


class Edge:
    ''' 边 '''

    def __init__(self, from_v: int, to_v: int, cap: int, cost: int) -> None:
        self.from_v = from_v  # 起点
        self.to_v = to_v  # 终点
        self.cap = cap  # 容量
        self.cost = cost  # 费用


class MCMF:

    def __init__(self, nv: int):
        """ nv 总顶点数 """
        self.g = [[] for _ in range(nv)]  # 图缓存
        self.h = [0] * nv  # 势能、点权，用以让 dijkstra 支持负权值
        self.prev_v = [0] * nv
        self.prev_e = [0] * nv
        self.nv = nv  # 总顶点数

    def add_edge(self, from_v: int, to_v: int, cost: int, cap: int) -> None:
        """ 增加一条边 start end是顶点索引 """
        self.g[from_v].append(Edge(len(self.g[to_v]), to_v, cap, cost))
        self.g[to_v].append(Edge(len(self.g[from_v]) - 1, from_v, 0, -cost))

    def min_cost_flow(self, src, tar, flow) -> int:
        """ 计算从src出发到tar，发出flow的流量的最小cost """
        res = 0
        while flow > 0:
            pq = []
            dis = [INF] * self.nv
            dis[src] = 0
            heappush(pq, [0, src])
            while pq:  # dijkstra
                curDis, cur = heappop(pq)
                if dis[cur] < curDis: continue
                for i in range(len(self.g[cur])):
                    nx: Edge = self.g[cur][i]
                    nd = dis[cur] + nx.cost + self.h[cur] - self.h[nx.to_v]
                    if nx.cap > 0 and dis[nx.to_v] > nd:
                        dis[nx.to_v] = nd
                        self.prev_v[nx.to_v] = cur
                        self.prev_e[nx.to_v] = i
                        heappush(pq, [dis[nx.to_v], nx.to_v])
            if dis[tar] == INF: return -1
            for i in range(self.nv):
                self.h[i] += dis[i]
            d = flow
            idx = tar
            while idx != src:
                d = min(d, self.g[self.prev_v[idx]][self.prev_e[idx]].cap)
                idx = self.prev_v[idx]
            flow -= d
            res += d * self.h[tar]
            idx = tar
            while idx != src:
                edge = self.g[self.prev_v[idx]][self.prev_e[idx]]
                edge.cap -= d
                self.g[idx][edge.from_v].cap += d
                idx = self.prev_v[idx]
        return res


######################## end ########################


class Solution:

    def minCost1(self, grid: List[List[int]]) -> int:
        # 费用流
        n, m = len(grid), len(grid[0])
        src, tar = 0, n * m - 1
        mcmf = MCMF(m * n)
        for i in range(n):
            for j in range(m):
                for k, (dx, dy) in enumerate([[0, 1], [0, -1], [1, 0], [-1, 0]]):
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1: continue
                    mcmf.add_edge(i * m + j, nx * m + ny, 0 if grid[i][j] == k + 1 else 1, 1)
        return mcmf.min_cost_flow(src, tar, 1)

    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nv = m * n
        g = [[] for _ in range(nv)]  # 图
        for i in range(n):
            for j in range(m):
                for k, (dx, dy) in enumerate([[0, 1], [0, -1], [1, 0], [-1, 0]]):
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1: continue
                    g[i * m + j].append([nx * m + ny, 0 if grid[i][j] == k + 1 else 1])

        # 迪克斯特拉
        def dijkstra(src: int, next_v: List[List[List[int]]]):
            dist, vis = [INF] * nv, [False] * nv
            dist[src] = 0
            q = [[0, src]]  # cost-v_idx
            while q:
                mn, idx = heappop(q)
                if vis[idx]: continue
                for nx_i, nx_c in next_v[idx]:
                    if nx_c + mn < dist[nx_i]:
                        dist[nx_i] = nx_c + mn
                        heappush(q, [dist[nx_i], nx_i])
                vis[idx] = True
            return dist

        dist = dijkstra(0, g)
        return dist[nv - 1]


if __name__ == '__main__':
    # 3
    print(Solution().minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
    # 0
    print(Solution().minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))
    # 1
    print(Solution().minCost([[1, 2], [4, 3]]))
    # 3
    print(Solution().minCost([[2, 2, 2], [2, 2, 2]]))
    # 0
    print(Solution().minCost([[4]]))