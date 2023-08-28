"""
 * 给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。
 * 部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。
 * 你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 10^9] 中的 正整数 ，使得从节点 source 到节点 destination 的 最短距离 为整数 target 。
 * 如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target ，你可以返回任意一种方案。
 * 如果存在使 source 到 destination 最短距离为 target 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。
 * 如果不存在这样的方案，请你返回一个 空数组 。
 * 注意：你不能修改一开始边权为正数的边。
 * 提示：
 * 1、1 <= n <= 100
 * 2、1 <= edges.length <= n * (n - 1) / 2
 * 3、edges[i].length == 3
 * 4、0 <= ai, bi < n
 * 5、wi = -1 或者 1 <= wi <= 10^7
 * 6、ai != bi
 * 7、0 <= source, destination < n
 * 8、source != destination
 * 9、1 <= target <= 10^9
 * 10、输入的图是连通图，且没有自环和重边。
 * 链接：https://leetcode.cn/problems/modify-graph-edge-weights/
"""
from typing import List
from heapq import heappush, heappop

INF = int(1e18)


class Solution:

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        z_pos = []
        g = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                z_pos.append(i)
                w = 1
            g[u].append((v, w))
            g[v].append((u, w))

        def dijkstra(src: int, next_v: List[List[List[int]]], flag):
            dist, vis = [INF] * n, [False] * n
            dist[src] = 0
            q = [[0, src]]  # cost-v_idx
            if flag == 0:
                pass
            else:
                pass
            while q:
                mn, idx = heappop(q)
                if vis[idx]: continue
                for nx_i, nx_c in next_v[idx]:
                    if nx_c + mn < dist[nx_i]:
                        dist[nx_i] = nx_c + mn
                        heappush(q, [dist[nx_i], nx_i])
                vis[idx] = True
            return dist

        dist0 = dijkstra(source, g, 0)
        if dist0[destination] > target: return []
        dist1 = dijkstra(source, g, 1)
        if dist1[destination] < target: return []
        return edges

    def modifiedGraphEdges1(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for i, (x, y, _) in enumerate(edges):
            g[x].append((y, i))
            g[y].append((x, i))  # 建图，额外保存边的编号

        dis = [[INF, INF] for _ in range(n)]
        dis[source] = [0, 0]

        def dijkstra(k: int) -> None:  # 这里 k 表示第一次/第二次
            vis = [False] * n
            while True:
                # 找到当前最短路，去更新它的邻居的最短路
                # 根据数学归纳法，dis[x][k] 一定是最短路长度
                x = -1
                for y, (b, d) in enumerate(zip(vis, dis)):
                    if not b and (x < 0 or d[k] < dis[x][k]):
                        x = y
                if x == destination:  # 起点 source 到终点 destination 的最短路已确定
                    return
                vis[x] = True  # 标记，在后续的循环中无需反复更新 x 到其余点的最短路长度
                for y, eid in g[x]:
                    wt = edges[eid][2]
                    if wt == -1:
                        wt = 1  # -1 改成 1
                    if k == 1 and edges[eid][2] == -1:
                        # 第二次 Dijkstra，改成 w
                        w = delta + dis[y][0] - dis[x][1]
                        if w > wt:
                            edges[eid][2] = wt = w  # 直接在 edges 上修改
                    # 更新最短路
                    dis[y][k] = min(dis[y][k], dis[x][k] + wt)

        dijkstra(0)
        delta = target - dis[destination][0]
        if delta < 0:  # -1 全改为 1 时，最短路比 target 还大
            return []

        dijkstra(1)
        if dis[destination][1] < target:  # 最短路无法再变大，无法达到 target
            return []

        for e in edges:
            if e[2] == -1:  # 剩余没修改的边全部改成 1
                e[2] = 1
        return edges


if __name__ == '__main__':
    # []
    print(Solution().modifiedGraphEdges(3, edges=[[0, 1, -1], [0, 2, 5]], source=0, destination=2, target=6))
    # [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
    print(Solution().modifiedGraphEdges(5, edges=[[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], source=0, destination=1, target=5))
    # [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
    print(Solution().modifiedGraphEdges(4, edges=[[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], source=0, destination=2, target=6))
