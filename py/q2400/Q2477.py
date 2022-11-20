"""
 * 给你一棵 n 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路。0 是首都。
 * 给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路 。
 * 每个城市里有一个代表，他们都要去首都参加一个会议。
 * 每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目。
 * 城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。
 * 请你返回到达首都最少需要多少升汽油。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、roads.length == n - 1
 * 3、roads[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 6、roads 表示一棵合法的树。
 * 7、1 <= seats <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/
"""
from typing import List


class Solution:

    def minimumFuelCost1(self, roads: List[List[int]], seats: int) -> int:
        # 思维转换
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for s, e in roads:
            g[s].append(e)
            g[e].append(s)

        ans = 0

        def dfs(x: int, fa: int) -> int:
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)
            if x:
                nonlocal ans
                ans += (size + seats - 1) // seats
            return size

        dfs(0, -1)
        return ans

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # 树状dp
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for s, e in roads:
            g[s].append(e)
            g[e].append(s)

        def dfs(x: int, fa: int):  # [cost-cnt]
            cost, cnt = 0, 1
            for nx in g[x]:
                if nx == fa: continue
                s, c = dfs(nx, x)
                cnt += c
                cost += s + (seats + c - 1) // seats  #  向上取整
            return cost, cnt

        return dfs(0, -1)[0]


if __name__ == '__main__':
    # 7
    print(Solution().minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))
    # 3
    print(Solution().minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5))
    # 0
    print(Solution().minimumFuelCost([], 1))
