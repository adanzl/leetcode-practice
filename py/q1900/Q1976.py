"""
 * 你在一个城市里，城市由 n 个路口组成，路口编号为 0 到 n - 1 ，某些路口之间有 双向 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。
 * 给你一个整数 n 和二维整数数组 roads ，其中 roads[i] = [ui, vi, time_i] 表示在路口 ui 和 vi 之间有一条需要花费 time_i 时间才能通过的道路。
 * 你想知道花费 最少时间 从路口 0 出发到达路口 n - 1 的方案数。
 * 请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= n <= 200
 * 2、n - 1 <= roads.length <= n * (n - 1) / 2
 * 3、roads[i].length == 3
 * 4、0 <= ui, vi <= n - 1
 * 5、1 <= time_i <= 10^9
 * 6、ui != vi
 * 7、任意两个路口之间至多有一条路。
 * 8、从任意路口出发，你能够到达其他任意路口。
 * 链接：https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/
"""
from typing import List
from heapq import heappush, heappop


class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        inf = int(1e18)
        MOD = 10**9 + 7
        g = [[] for _ in range(n)]
        dis, vis, cnt = [inf] * n, [False] * n, [0] * n
        dis[0] = 0
        cnt[0] = 1
        for s, e, c in roads:
            g[s].append([e, c])
            g[e].append([s, c])
        q = [[0, 0]]
        while q:
            mn_cost, idx = heappop(q)
            if vis[idx]: continue
            vis[idx] = True
            for nx_i, nx_c in g[idx]:
                nc = nx_c + mn_cost
                if nc < dis[nx_i]:
                    cnt[nx_i] = cnt[idx]
                    dis[nx_i] = nc
                    heappush(q, [nc, nx_i])
                elif nc == dis[nx_i]:
                    cnt[nx_i] += cnt[idx]
        return cnt[-1] % MOD


if __name__ == '__main__':
    # 4
    print(Solution().countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]))
    # 1
    print(Solution().countPaths(2, [[1, 0, 10]]))