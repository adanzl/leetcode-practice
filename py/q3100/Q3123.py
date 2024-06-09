"""
 * 给你一个 n 个节点的无向带权图，节点编号为 0 到 n - 1 。
 * 图中总共有 m 条边，用二维数组 edges 表示，其中 edges[i] = [a_i, b_i, w_i] 表示节点 a_i 和  b_i 之间有一条边权为 w_i 的边。
 * 对于节点 0 为出发点，节点 n - 1 为结束点的所有最短路，你需要返回一个长度为 m 的 boolean 数组 answer ，
 * 如果 edges[i] 至少 在其中一条最短路上，那么 answer[i] 为 true ，否则 answer[i] 为 false 。
 * 请你返回数组 answer 。
 * 注意，图可能不连通。
 * 提示：
 * 1、2 <= n <= 5 * 10^4
 * 2、m == edges.length
 * 3、1 <= m <= min(5 * 10^4, n * (n - 1) / 2)
 * 4、0 <= a_i, b_i < n
 * 5、a_i !=  b_i
 * 6、1 <= w_i <= 10^5
 * 7、图中没有重边。
 * 链接：https://leetcode.cn/problems/find-edges-in-shortest-paths/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            g[u].append([v, w, i])
            g[v].append([u, w, i])

        INF = int(1e18)

        def dijkstra(src: int, next_v: List[List[List[int]]]):
            dist, vis, path = [INF] * n, [False] * n, [set() for _ in range(n)]
            dist[src] = 0
            q = [[0, src]]  # cost-v_idx
            while q:
                mn, idx = heappop(q)
                if vis[idx]: continue
                for nx_i, nx_c, nx_e in next_v[idx]:
                    if nx_c + mn < dist[nx_i]:
                        dist[nx_i] = nx_c + mn
                        heappush(q, [dist[nx_i], nx_i])
                        path[nx_i] = set([nx_e])
                    if nx_c + mn == dist[nx_i]:
                        path[nx_i].add(nx_e)
                vis[idx] = True
            return dist, path

        dis_0, path_0 = dijkstra(0, g)
        dis_n, path_n = dijkstra(n - 1, g)
        mn_dis = dis_0[n - 1]
        ans = [False] * len(edges)
        for i in range(n):
            if dis_0[i] + dis_n[i] == mn_dis:
                for v in path_0[i]:
                    ans[v] = True
                for v in path_n[i]:
                    ans[v] = True
        return ans


if __name__ == '__main__':
    # [false,false,false,false,false,false,true,false,false,false]
    print(Solution().findAnswer(
        7,
        [[2, 4, 4], [5, 4, 9], [0, 2, 6], [6, 2, 1], [3, 6, 3], [1, 3, 6], [6, 0, 4], [0, 4, 5], [1, 0, 1], [3, 5, 2]]))
    # [true,true,true,false,true,true,true,false]
    print(Solution().findAnswer(
        6, [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]))
    # [true,false,false,true]
    print(Solution().findAnswer(4, edges=[[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]))
