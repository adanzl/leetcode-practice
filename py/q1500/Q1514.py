"""
 * 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 sucProb[i] 。
 * 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
 * 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。
 * 提示：
 * 1、2 <= n <= 10^4
 * 2、0 <= start, end < n
 * 3、start != end
 * 4、0 <= a, b < n
 * 5、a != b
 * 6、0 <= sucProb.length == edges.length <= 2*10^4
 * 7、0 <= sucProb[i] <= 1
 * 8、每两个节点之间最多有一条边
 * 链接：https://leetcode.cn/problems/path-with-maximum-probability/
"""
from typing import List
from heapq import heappop, heappush


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], sucProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i, (s, e) in enumerate(edges):
            g[s].append([e, sucProb[i]])  # idx-prob
            g[e].append([s, sucProb[i]])

        def dijkstra(src, next_v):
            prob, vis = [0.0] * n, [False] * n
            q = [[-1, src]]  # mx_prob-idx
            while q:
                mx_prob, idx = heappop(q)
                mx_prob = -mx_prob
                if vis[idx]: continue
                vis[idx] = True
                for nx_i, nx_prob in next_v[idx]:
                    n_p = mx_prob * nx_prob
                    if n_p > prob[nx_i]:
                        prob[nx_i] = n_p
                        heappush(q, [-n_p, nx_i])
            return prob

        return dijkstra(start, g)[end]


if __name__ == '__main__':
    # 0.25
    print(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
    # 0.3
    print(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
    # 0.0
    print(Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2))
