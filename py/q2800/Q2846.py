"""
 * 现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，
 * 其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。
 * 另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。
 * 对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。
 * 在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。
 * 注意：
 * 1、查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。
 * 2、从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。
 * 返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、edges.length == n - 1
 * 3、edges[i].length == 3
 * 4、0 <= ui, vi < n
 * 5、1 <= wi <= 26
 * 6、生成的输入满足 edges 表示一棵有效的树
 * 7、1 <= queries.length == m <= 2 * 10^4
 * 8、queries[i].length == 2
 * 9、0 <= ai, bi < n
 * 链接：https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
"""
from typing import List


class Solution:

    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        nxt = [[] for _ in range(n)]
        for u, v, w in edges:
            nxt[u].append([v, w])
            nxt[v].append([u, w])
        cnt = [[] for _ in range(n)]
        cnt[0] = [0] * 27
        dep = [0] * n  # 深度
        f = [[-1 for __ in range(31)] for _ in range(n)]  # idx-i, idx 的2^i级父节点

        def dfs(idx, fa):
            i = 1  # 倍增构建父节点
            while (1 << i) <= dep[idx]:
                f[idx][i] = f[f[idx][i - 1]][i - 1]
                i += 1
            for nx, w in nxt[idx]:
                if nx == fa: continue
                f[nx][0] = idx
                dep[nx] = dep[idx] + 1
                cnt[nx] = cnt[idx][:]
                cnt[nx][w] += 1
                dfs(nx, idx)

        def lca(u, v):  # 最近公共祖先
            if dep[u] < dep[v]: u, v = v, u  # dep[u] >= dep[v]
            for i in range(30, -1, -1):  # 对齐uv深度
                if f[u][i] >= 0 and dep[f[u][i]] >= dep[v]:
                    u = f[u][i]
                if u == v: return u
            for i in range(30, -1, -1):
                if f[u][i] != f[v][i]:
                    u = f[u][i]
                    v = f[v][i]
            return f[u][0]

        dfs(0, 0)
        ans = []
        for _, (u, v) in enumerate(queries):
            fa = lca(u, v)
            lu, lv = dep[u] - dep[fa], dep[v] - dep[fa]
            a = 10**10
            for i in range(27):
                cu, cv = cnt[u][i] - cnt[fa][i], cnt[v][i] - cnt[fa][i]
                a = min(a, lu - cu + lv - cv)
            ans.append(a)
        return ans


if __name__ == '__main__':
    # [1,0,0,0,0,0]
    print(Solution().minOperationsQueries(3, [[2, 1, 1], [2, 0, 2]], [[0, 1], [0, 2], [1, 2], [0, 0], [1, 1], [2, 2]]))
    # [0,0,1,3]
    print(Solution().minOperationsQueries(7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]], queries=[[0, 3], [3, 6], [2, 6], [0, 6]]))
    # [1,2,2,3]
    print(Solution().minOperationsQueries(8, edges=[[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]], queries=[[4, 6], [0, 4], [6, 5], [7, 4]]))