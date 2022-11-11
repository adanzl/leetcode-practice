"""
 * 给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。
 * 图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnt_i] 表示原始图中节点 ui 和 vi 之间存在一条边，cnt_i 是将边 细分 后的新节点总数。
 * 注意，cnt_i == 0 表示边不可细分。
 * 要 细分 边 [ui, vi] ，需要将其替换为 (cnt_i + 1) 条新边，和 cnt_i 个新节点。新节点为 x1, x2, ... ，
 * 新边为 [ui, x1], [x1, x2], [x2, x3], ... 。
 * 现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。
 * 给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。
 * 提示：
 * 1、0 <= edges.length <= min(n * (n - 1) / 2, 10^4)
 * 2、edges[i].length == 3
 * 3、0 <= ui < vi < n
 * 4、图中 不存在平行边
 * 5、0 <= cnt_i <= 10^4
 * 6、0 <= maxMoves <= 10^9
 * 7、1 <= n <= 3000
 * 链接：https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/
"""
from typing import List
from heapq import heappush, heappop

INF = int(1e18)


class Solution:

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:

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

        g = [[] for _ in range(n)]
        for s, e, c in edges:
            g[s].append([e, c + 1])
            g[e].append([s, c + 1])
        ans = 0
        dist = dijkstra(0, g)
        for d in dist:
            if d <= maxMoves: ans += 1
        for s, e, c in edges:
            c1 = max(0, maxMoves - dist[s])
            c2 = max(0, maxMoves - dist[e])
            ans += min(c1 + c2, c)
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3))
    # 23
    print(Solution().reachableNodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4))
    # 1
    print(Solution().reachableNodes([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5))
