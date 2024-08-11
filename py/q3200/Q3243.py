"""
 * 给你一个整数 n 和一个二维整数数组 queries。
 * 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
 * queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
 * 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，
 * answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。
 * 提示：
 * 1、3 <= n <= 500
 * 2、1 <= queries.length <= 500
 * 3、queries[i].length == 2
 * 4、0 <= queries[i][0] < queries[i][1] < n
 * 5、1 < queries[i][1] - queries[i][0]
 * 6、查询中没有重复的道路。
 * 链接：https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append([i + 1, 1])

        INF = int(1e18)

        def dijkstra(src: int, next_v: List[List[List[int]]]):
            dist, vis = [INF] * n, [False] * n
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

        ans = []
        for u, v in queries:
            g[u].append([v, 1])
            dist = dijkstra(0, g)
            ans.append(dist[-1])
        return ans


if __name__ == '__main__':
    # [3, 2, 1]
    print(Solution().shortestDistanceAfterQueries(5, queries=[[2, 4], [0, 2], [0, 4]]))
    # [1, 1]
    print(Solution().shortestDistanceAfterQueries(4, queries=[[0, 3], [0, 2]]))
