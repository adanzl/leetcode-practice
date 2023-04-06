"""
 * 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。
 * 图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边。
 * 每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。
 * 返回图中 最短 环的长度。如果不存在环，则返回 -1 。
 * 环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、1 <= edges.length <= 1000
 * 3、edges[i].length == 2
 * 4、0 <= ui, vi < n
 * 5、ui != vi
 * 6、不存在重复的边
 * 链接：https://leetcode.cn/problems/shortest-cycle-in-a-graph/
"""
from typing import List


class Solution:

    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        ans = n + 1
        g = [[] for _ in range(n)]
        for u, nx in edges:
            g[u].append(nx)
            g[nx].append(u)
        for i in range(n):
            vis = [-1] * n
            vis[i] = 0
            dis = 1
            q = [[i, -1]]
            while q:
                t = q[:]
                q = []
                for idx, fa in t:
                    for nx in g[idx]:
                        if nx == fa: continue
                        if vis[nx] != -1:
                            ans = min(ans, dis + vis[nx])
                        else:
                            vis[nx] = dis
                            q.append([nx, idx])
                dis += 1
        return -1 if ans == n + 1 else ans


if __name__ == '__main__':
    # 3
    print(Solution().findShortestCycle(7, edges=[[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]))
    # -1
    print(Solution().findShortestCycle(4, edges=[[0, 1], [0, 2]]))
