"""
 * 给你一个正整数 n ，表示一个 无向 图中的节点数目，节点编号从 1 到 n 。
 * 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 双向 边。注意给定的图可能是不连通的。
 * 请你将图划分为 m 个组（编号从 1 开始），满足以下要求：
 * 1、图中每个节点都只属于一个组。
 * 2、图中每条边连接的两个点 [ai, bi] ，如果 ai 属于编号为 x 的组，bi 属于编号为 y 的组，那么 |y - x| = 1 。
 * 请你返回最多可以将节点分为多少个组（也就是最大的 m ）。如果没办法在给定条件下分组，请你返回 -1 。
 * 提示：
 * 1、1 <= n <= 500
 * 2、1 <= edges.length <= 10^4
 * 3、edges[i].length == 2
 * 4、1 <= ai, bi <= n
 * 5、ai != bi
 * 6、两个点之间至多只有一条边。
 * 链接：https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/
"""
from collections import defaultdict
from typing import Deque, List
#
# @lc app=leetcode.cn id=2493 lang=python3
#
# [2493] 将节点分成尽可能多的组
#

# @lc code=start


class Solution:

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # 良久之后的重写，还真过了~
        nxt = [[] for _ in range(n)]
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            u, v = u - 1, v - 1
            r0, r1 = find(u), find(v)
            if r0 != r1:
                parent[r1] = r0
            nxt[u].append(v)
            nxt[v].append(u)
        group = defaultdict(list)
        for i in range(n):
            group[find(i)].append(i)
        ans = 0

        def min_group(lst):
            ret = -1
            for s in lst:
                ll = 0
                vis = defaultdict(lambda: -1)
                q = [[s, -1]]
                vis[s] = 0
                b = False
                while q and not b:
                    t = []
                    for v, fa in q:
                        for nx in nxt[v]:
                            if fa == nx: continue
                            if 0 <= vis[nx]:
                                if vis[nx] == ll:
                                    ll = -1
                                    b = True
                                    break
                                else:
                                    continue
                            vis[nx] = ll + 1
                            t.append([nx, v])
                        if b: break
                    if b: break
                    q = t
                    ll += 1
                ret = max(ret, ll)
            return ret

        for lst in group.values():
            v = min_group(lst)
            if v == -1:
                return -1
            ans += v
        return ans


# @lc code=end

    def magnificentSets1(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        def bfs(start: int) -> int:
            mx = 0
            group = {start: base}
            q = Deque([(start, base)])
            while q:
                x, id = q.popleft()
                mx = max(mx, id)
                for y in g[x]:
                    if y not in group:
                        group[y] = id + 1
                        q.append((y, id + 1))
                    elif abs(group[y] - group[x]) != 1:
                        return 0
            return mx

        ans = 0
        vis = [False] * n
        for i, b in enumerate(vis):
            if b: continue
            base = ans + 1

            def dfs(x: int) -> None:
                nonlocal ans
                ans = max(ans, bfs(x))
                vis[x] = True
                for y in g[x]:
                    if not vis[y]:
                        dfs(y)

            dfs(i)
            if ans < base: return -1  # ans 没有变大，说明无法找到合法的分组
        return ans

    def magnificentSets2(self, n: int, edges: List[List[int]]) -> int:
        # 这玩意美服会超时
        g = [[] for _ in range(n)]  # 图
        for s, e in edges:
            g[s - 1].append(e - 1)
            g[e - 1].append(s - 1)

        vis = [0] * n
        ans = 0

        for i in range(n):
            if vis[i]: continue
            # 首先找出连通块
            vis[i] = 1
            q = Deque([i])
            pts = [i]  # 包含 i 的连通块的集合
            while q:
                idx = q.popleft()
                for nx in g[idx]:
                    if vis[nx]: continue
                    vis[nx] = 1
                    q.append(nx)
                    pts.append(nx)

            # 在当前连通块里求最大分组数
            size = -1
            for center in pts:
                dist = [-1] * n
                dist[center] = 0
                q.append(center)
                while q:
                    idx = q.popleft()
                    for nx in g[idx]:
                        if dist[nx] == -1:
                            dist[nx] = dist[idx] + 1
                            q.append(nx)
                for s, e in edges:  # 验证每条边的正确性
                    if dist[s - 1] != -1 and dist[e - 1] != -1 and dist[s - 1] == dist[e - 1]:
                        return -1  # 如果当前连通块里没有符合条件的，返回 -1
                for pt in pts:
                    size = max(size, dist[pt] + 1)
            # 答案是所有的连通块的答案之和
            ans += size
        return ans

if __name__ == '__main__':
    # 4
    print(Solution().magnificentSets(6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]))
    # -1
    print(Solution().magnificentSets(3, [[1, 2], [2, 3], [3, 1]]))
