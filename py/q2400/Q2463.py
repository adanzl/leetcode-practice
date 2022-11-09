"""
 * X 轴上有一些机器人和工厂。给你一个整数数组 robot ，其中 robot[i] 是第 i 个机器人的位置。再给你一个二维整数数组 factory ，
 * 其中 factory[j] = [position_j, limit_j] ，表示第 j 个工厂的位置在 position_j ，且第 j 个工厂最多可以修理 limit_j 个机器人。
 * 每个机器人所在的位置 互不相同 。每个工厂所在的位置也 互不相同 。注意一个机器人可能一开始跟一个工厂在 相同的位置 。
 * 所有机器人一开始都是坏的，他们会沿着设定的方向一直移动。设定的方向要么是 X 轴的正方向，要么是 X 轴的负方向。当一个机器人经过一个没达到上限的工厂时，这个工厂会维修这个机器人，且机器人停止移动。
 * 任何时刻，你都可以设置 部分 机器人的移动方向。你的目标是最小化所有机器人总的移动距离。
 * 请你返回所有机器人移动的最小总距离。测试数据保证所有机器人都可以被维修。
 * 注意：
 * 1、所有机器人移动速度相同。
 * 2、如果两个机器人移动方向相同，它们永远不会碰撞。
 * 3、如果两个机器人迎面相遇，它们也不会碰撞，它们彼此之间会擦肩而过。
 * 4、如果一个机器人经过了一个已经达到上限的工厂，机器人会当作工厂不存在，继续移动。
 * 5、机器人从位置 x 到位置 y 的移动距离为 |y - x| 。
 * 提示：
 * 1、1 <= robot.length, factory.length <= 100
 * 2、factory[j].length == 2
 * 3、-10^9 <= robot[i], position_j <= 10^9
 * 4、0 <= limit_j <= robot.length
 * 5、测试数据保证所有机器人都可以被维修。
 * 链接：https://leetcode.cn/problems/minimum-total-distance-traveled/
"""
from functools import cache
from heapq import heappop, heappush
from typing import Deque, List, Tuple

######################## Template ########################
# 最小费用最大流


class Edge:
    ''' 边 '''

    def __init__(self, from_v: int, to_v: int, cap: int, cost: int, flow=0) -> None:
        self.from_v = from_v  # 起点
        self.to_v = to_v  # 终点
        self.cap = cap  # 容量
        self.cost = cost  # 费用
        self.flow = flow  # 已经使用的流量


INF = int(1e18)


class MinCostMaxFlow:
    """最小费用流的连续最短路算法复杂度为流量*最短路算法复杂度"""

    __slots__ = ("_n", "_start", "_end", "_edges", "_reGraph", "_dist", "_visited", "_curEdges")

    def __init__(self, n: int, start: int, end: int):
        """
        Args:
            n (int): 包含虚拟点在内的总点数
            start (int): (虚拟)源点
            end (int): (虚拟)汇点
        """
        assert 0 <= start < n and 0 <= end < n
        self._n = n
        self._start = start
        self._end = end
        self._edges: List["Edge"] = []
        self._reGraph: List[List[int]] = [[] for _ in range(n + 10)]  # 残量图存储的是边的下标

        self._dist = [INF] * (n + 10)
        self._visited = [False] * (n + 10)
        self._curEdges = [0] * (n + 10)

    def add_edge(self, from_v: int, to_v: int, cap: int, cost: int) -> None:
        """原边索引为i 反向边索引为i^1"""
        self._edges.append(Edge(from_v, to_v, cap, cost, 0))
        self._edges.append(Edge(to_v, from_v, 0, -cost, 0))
        len_ = len(self._edges)
        self._reGraph[from_v].append(len_ - 2)
        self._reGraph[to_v].append(len_ - 1)

    def work(self) -> Tuple[int, int]:
        """
        Returns:
            Tuple[int, int]: [最大流,最小费用]
        """
        maxFlow, minCost = 0, 0
        while self._spfa():
            # !如果流量限定为1，那么一次dfs只会找到一条费用最小的增广流
            # !如果流量限定为INF，那么一次dfs不只会找到一条费用最小的增广流
            flow = self._dfs(self._start, self._end, INF)
            maxFlow += flow
            minCost += flow * self._dist[self._end]
        return maxFlow, minCost

    def slope(self) -> List[Tuple[int, int]]:
        """
        Returns:
            List[Tuple[int, int]]: 流量为a时,最小费用是b
        """
        res = [(0, 0)]
        flow, cost = 0, 0
        while self._spfa():
            deltaFlow = self._dfs(self._start, self._end, INF)
            flow += deltaFlow
            cost += deltaFlow * self._dist[self._end]
            res.append((flow, cost))  # type: ignore
        return res

    def _spfa(self) -> bool:
        """spfa沿着最短路寻找增广路径  有负cost的边不能用dijkstra"""
        n, start, end, edges, reGraph, visited = (
            self._n,
            self._start,
            self._end,
            self._edges,
            self._reGraph,
            self._visited,
        )

        self._curEdges = [0] * n
        self._dist = dist = [INF] * n
        dist[start] = 0
        queue = Deque([start])

        while queue:
            cur = queue.popleft()
            visited[cur] = False
            for edgeIndex in reGraph[cur]:
                edge = edges[edgeIndex]
                cost, remain, next = edge.cost, edge.cap - edge.flow, edge.to_v
                if remain > 0 and dist[cur] + cost < dist[next]:
                    dist[next] = dist[cur] + cost
                    if not visited[next]:
                        visited[next] = True
                        if queue and dist[queue[0]] > dist[next]:
                            queue.appendleft(next)
                        else:
                            queue.append(next)

        return dist[end] != INF

    def _dfs(self, cur: int, end: int, flow: int) -> int:
        if cur == end:
            return flow

        visited, reGraph, curEdges, edges, dist = (
            self._visited,
            self._reGraph,
            self._curEdges,
            self._edges,
            self._dist,
        )

        visited[cur] = True
        res = flow
        index = curEdges[cur]
        while res and index < len(reGraph[cur]):
            edgeIndex = reGraph[cur][index]
            next, remain = edges[edgeIndex].to_v, edges[edgeIndex].cap - edges[edgeIndex].flow
            if remain > 0 and not visited[next] and dist[next] == dist[cur] + edges[edgeIndex].cost:
                delta = self._dfs(next, end, remain if remain < res else res)
                res -= delta
                edges[edgeIndex].flow += delta
                edges[edgeIndex ^ 1].flow -= delta
            curEdges[cur] += 1
            index = curEdges[cur]

        visited[cur] = False
        return flow - res


class MCMF:

    def __init__(self, nv: int):
        """ nv 总顶点数 """
        self.g = [[] for _ in range(nv)]  # 图缓存
        self.h = [0] * nv  # 赋权，用以让 dijkstra 支持负权值
        self.prev_v = [0] * nv
        self.prev_e = [0] * nv
        self.nv = nv  # 总顶点数

    def add_edge(self, start: int, end: int, cost: int, cap: int) -> None:
        """ 增加一条边 start end是顶点索引 """
        self.g[start].append(Edge(len(self.g[end]), end, cap, cost))
        self.g[end].append(Edge(len(self.g[start]) - 1, start, 0, -cost))

    def min_cost_flow(self, src, tar, flow) -> int:
        """ 计算从src出发到tar，发出flow的流量的最小cost """
        res = 0
        while flow > 0:
            pq = []
            dis = [INF] * self.nv
            dis[src] = 0
            heappush(pq, [0, src])
            while pq:  # dijkstra
                curDis, cur = heappop(pq)
                if dis[cur] < curDis: continue
                for i in range(len(self.g[cur])):
                    nx: Edge = self.g[cur][i]
                    nd = dis[cur] + nx.cost + self.h[cur] - self.h[nx.to_v]
                    if nx.cap > 0 and dis[nx.to_v] > nd:
                        dis[nx.to_v] = nd
                        self.prev_v[nx.to_v] = cur
                        self.prev_e[nx.to_v] = i
                        heappush(pq, [dis[nx.to_v], nx.to_v])
            if dis[tar] == INF: return -1
            for i in range(self.nv):
                self.h[i] += dis[i]
            d = flow
            idx = tar
            while idx != src:
                d = min(d, self.g[self.prev_v[idx]][self.prev_e[idx]].cap)
                idx = self.prev_v[idx]
            flow -= d
            res += d * self.h[tar]
            idx = tar
            while idx != src:
                edge = self.g[self.prev_v[idx]][self.prev_e[idx]]
                edge.cap -= d
                self.g[idx][edge.from_v].cap += d
                idx = self.prev_v[idx]
        return res


######################## end ########################


class Solution:

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        return self.minimumTotalDistance4(robot, factory)

    # 邻项交换法，证明贪心，每个工厂要维修的机器人是连续的
    def minimumTotalDistance1(self, robot: List[int], factory: List[List[int]]) -> int:
        # dp压缩，背包问题
        rn, fn = len(robot), len(factory)
        robot.sort()
        factory.sort()
        dp = [0] + [INF] * rn
        pre = 0
        for x, limit in factory:
            for j in range(rn, 0, -1):  # 最后一个维修机器人的索引+1
                # 此处要倒序遍历，由于每次增加一个factory会增加一个limit，如果正向遍历，dp[i]的值依赖dp[i-1]，dp[i+limit]会计算错误
                cost = 0
                for k in range(1, limit + 1):  # 最新的工厂修几个
                    cost += abs(x - robot[j - k])
                    dp[j] = min(dp[j], dp[j - k] + cost)
        return int(dp[-1])

    def minimumTotalDistance2(self, robot: List[int], factory: List[List[int]]) -> int:
        # dp[i][j] i开始(包含），后面的工厂修理 j 个机器人(包含）后面的机器人，的最小移动距离
        rn, fn = len(robot), len(factory)
        robot.sort()
        factory.sort()

        @cache
        def dfs(fi, ri):
            if ri == rn: return 0
            if fi > fn - 1: return INF
            xf, limit = factory[fi]
            if fi == fn - 1:  #  这个if是一个剪枝，大约减少50%时间
                if rn - ri > limit: return INF
                return sum(abs(x - xf) for x in robot[ri:])
            ret = dfs(fi + 1, ri)  # 当前工厂不修理
            cost = 0
            for k in range(1, min(limit, rn - ri) + 1):
                cost += abs(robot[ri + k - 1] - xf)
                ret = min(ret, dfs(fi + 1, ri + k) + cost)
            return ret

        return int(dfs(0, 0))

    # 费用流 spfa
    def minimumTotalDistance3(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        START, END = n + m + 3, n + m + 4
        obj = MinCostMaxFlow(n + m + 10, START, END)
        for i in range(n):
            obj.add_edge(START, i, 1, 0)
        for i in range(n):
            for j in range(m):
                obj.add_edge(i, n + j, 1, abs(robot[i] - factory[j][0]))
        for i in range(m):
            obj.add_edge(n + i, END, factory[i][1], 0)
        return int(obj.work()[1])

    # 费用流 dijkstra
    def minimumTotalDistance4(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)  # 顶点下标 [0]-[n-1]是robot [n]-[n+m-1]是factory 再后面是起点和终点
        src, tar = n + m, n + m + 1
        mcmf = MCMF(n + m + 2)
        for i in range(n):
            mcmf.add_edge(src, i, cost=0, cap=1)
        for i in range(m):
            mcmf.add_edge(n + i, tar, 0, factory[i][1])
        for i in range(n):
            for j in range(m):
                mcmf.add_edge(i, n + j, abs(robot[i] - factory[j][0]), 1)
        return mcmf.min_cost_flow(src, tar, n)


if __name__ == '__main__':
    # 6
    print(Solution().minimumTotalDistance([9, 11, 99, 101], [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]]))
    # 4
    print(Solution().minimumTotalDistance([0, 4, 6], factory=[[2, 2], [6, 2]]))
    # 2
    print(Solution().minimumTotalDistance([1, -1], factory=[[-2, 1], [2, 1]]))
    # 4412966458
    print(Solution().minimumTotalDistance(
        [-333539942, 359275673, 89966494, 949684497, -733065249, 241002388, 325009248, 403868412, -390719486, -670541382, 563735045, 119743141, 323190444, 534058139, -684109467, 425503766, 761908175],
        [[-590277115, 0], [-80676932, 3], [396659814, 0], [480747884, 9], [118956496, 10]]))