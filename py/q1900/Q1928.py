"""
 * 一个国家有 n 个城市，城市编号为 0 到 n - 1 ，题目保证 所有城市 都由双向道路 连接在一起 。
 * 道路由二维整数数组 edges 表示，其中 edges[i] = [xi, yi, time_i] 表示城市 xi 和 yi 之间有一条双向道路，耗费时间为 time_i 分钟。
 * 两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。
 * 每次经过一个城市时，你需要付通行费。通行费用一个长度为 n 且下标从 0 开始的整数数组 passingFees 表示，其中 passingFees[j] 是你经过城市 j 需要支付的费用。
 * 一开始，你在城市 0 ，你想要在 maxTime 分钟以内 （包含 maxTime 分钟）到达城市 n - 1 。旅行的 费用 为你经过的所有城市 通行费之和 （包括 起点和终点城市的通行费）。
 * 给你 maxTime，edges 和 passingFees ，请你返回完成旅行的 最小费用 ，如果无法在 maxTime 分钟以内完成旅行，请你返回 -1 。
 * 提示：
 * 1、1 <= maxTime <= 1000
 * 2、n == passingFees.length
 * 3、2 <= n <= 1000
 * 4、n - 1 <= edges.length <= 1000
 * 5、0 <= xi, yi <= n - 1
 * 6、1 <= time_i <= 1000
 * 7、1 <= passingFees[j] <= 1000 
 * 8、图中两个节点之间可能有多条路径。
 * 9、图中不含有自环。
 * 链接：https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/
"""
from collections import defaultdict
from typing import List
from heapq import heappush, heappop

INF = int(1E15)


class Solution:

    def minCost1(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # 分层图
        nv = len(passingFees)
        g = [[] for _ in range(nv)]
        costs, vis = defaultdict(lambda: INF), set()
        for s, e, t in edges:
            g[s].append([e, t])
            g[e].append([s, t])
        q = [[passingFees[0], maxTime, 0]]  # fee-time_remain-idx
        while q:
            f, t, idx = heappop(q)
            if (idx, t) in vis: continue
            vis.add((idx, t))
            for nx_i, nx_t in g[idx]:
                if t < nx_t: continue
                nf = f + passingFees[nx_i]
                if nx_i == nv - 1: return nf
                if costs[(nx_i, t - nx_t)] > nf:
                    costs[(nx_i, t - nx_t)] = nf
                    heappush(q, [nf, t - nx_t, nx_i])
        return -1

    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # 动态规划
        nv = len(passingFees)
        dp = [[INF] * nv for _ in range(maxTime + 1)]  # dp[t][i] time t reach i min cost
        dp[0][0] = passingFees[0]
        for mt in range(maxTime + 1):
            for s, e, t in edges:
                if t > mt: continue
                dp[mt][e] = min(dp[mt][e], dp[mt - t][s] + passingFees[e])
                dp[mt][s] = min(dp[mt][s], dp[mt - t][e] + passingFees[s])
        ans = min(dp[t][-1] for t in range(maxTime + 1))
        return -1 if ans == INF else ans


if __name__ == '__main__':
    # 11
    print(Solution().minCost(30, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]))
    # 48
    print(Solution().minCost(29, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]))
    # -1
    print(Solution().minCost(25, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]))
