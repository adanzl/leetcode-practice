"""
 * 给你一个二维数组 edges 表示一个 n 个点的无向图，
 * 其中 edges[i] = [u_i, v_i, length_i] 表示节点 u_i 和节点 v_i 之间有一条需要 length_i 单位时间通过的无向边。
 * 同时给你一个数组 disappear ，其中 disappear[i] 表示节点 i 从图中消失的时间点，在那一刻及以后，你无法再访问这个节点。
 * 注意，图有可能一开始是不连通的，两个节点之间也可能有多条边。
 * 请你返回数组 answer ，answer[i] 表示从节点 0 到节点 i 需要的 最少 单位时间。
 * 如果从节点 0 出发 无法 到达节点 i ，那么 answer[i] 为 -1 。
 * 提示：
 * 1、1 <= n <= 5 * 10^4
 * 2、0 <= edges.length <= 10^5
 * 3、edges[i] == [u_i, v_i, length_i]
 * 4、0 <= ui, vi <= n - 1
 * 5、1 <= length_i <= 10^5
 * 6、disappear.length == n
 * 7、1 <= disappear[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        INF = int(1e18)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])
        ans = [-1] * n
        ans[0] = 0

        def dijkstra(src: int, next_v: List[List[List[int]]]):
            dist, vis = [INF] * n, [False] * n
            dist[src] = 0
            q = [[0, src]]  # cost-v_idx
            while q:
                mn, idx = heappop(q)
                if vis[idx]: continue
                for nx_i, nx_c in next_v[idx]:
                    if nx_c + mn >= disappear[nx_i]:
                        continue
                    if nx_c + mn < dist[nx_i]:
                        dist[nx_i] = nx_c + mn
                        heappush(q, [dist[nx_i], nx_i])
                vis[idx] = True
            return dist

        ans = dijkstra(0, g)
        return [v if v != INF else -1 for v in ans]


if __name__ == '__main__':
    # [0,2,3]
    print(Solution().minimumTime(3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 3, 5]))
    # [0,-1]
    print(Solution().minimumTime(2, edges=[[0, 1, 1]], disappear=[1, 1]))
    # [0,-1,4]
    print(Solution().minimumTime(3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5]))
