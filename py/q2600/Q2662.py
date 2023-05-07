"""
 * 给你一个数组 start ，其中 start = [startX, startY] 表示你的初始位置位于二维空间上的 (startX, startY) 。
 * 另给你一个数组 target ，其中 target = [targetX, targetY] 表示你的目标位置 (targetX, targetY) 。
 * 从位置 (x1, y1) 到空间中任一其他位置 (x2, y2) 的代价是 |x2 - x1| + |y2 - y1| 。
 * 给你一个二维数组 specialRoads ，表示空间中存在的一些特殊路径。
 * 其中 specialRoads[i] = [x1_i, y1_i, x2_i, y2_i, cost_i] 表示第 i 条特殊路径可以从 (x1i, y1i) 到 (x2i, y2i) ，但成本等于 cost_i 。
 * 你可以使用每条特殊路径任意次数。
 * 返回从 (startX, startY) 到 (targetX, targetY) 所需的最小代价。
 * 提示：
 * 1、start.length == target.length == 2
 * 2、1 <= startX <= targetX <= 10^5
 * 3、1 <= startY <= targetY <= 10^5
 * 4、1 <= specialRoads.length <= 200
 * 5、specialRoads[i].length == 5
 * 6、startX <= x1_i, x2_i <= targetX
 * 7、startY <= y1_i, y2_i <= targetY
 * 8、1 <= cost_i <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def minimumCost(self, start: List[int], target: List[int], sr: List[List[int]]) -> int:
        n = len(sr)
        nn = n * 2 + 2
        g = [[] for _ in range(nn)]  # n*2:start, n*2+1:target

        def add_edge(i, j, c):
            g[i].append([j, c])
            g[j].append([i, c])

        add_edge(n * 2, n * 2 + 1, abs(start[0] - target[0]) + abs(start[1] - target[1]))
        for i, (x1, y1, x2, y2, cost) in enumerate(sr):
            add_edge(n * 2, i * 2, abs(x1 - start[0]) + abs(y1 - start[1]))
            add_edge(n * 2, i * 2 + 1, abs(x2 - start[0]) + abs(y2 - start[1]))
            add_edge(n * 2 + 1, i * 2, abs(x1 - target[0]) + abs(y1 - target[1]))
            add_edge(n * 2 + 1, i * 2 + 1, abs(x2 - target[0]) + abs(y2 - target[1]))
            g[i * 2].append([i * 2 + 1, cost])

        for i in range(n):
            for j in range(i + 1, n):
                add_edge(i * 2, j * 2, abs(sr[i][0] - sr[j][0]) + abs(sr[i][1] - sr[j][1]))
                add_edge(i * 2, j * 2 + 1, abs(sr[i][0] - sr[j][2]) + abs(sr[i][1] - sr[j][3]))
                add_edge(i * 2 + 1, j * 2, abs(sr[i][2] - sr[j][0]) + abs(sr[i][3] - sr[j][1]))
                add_edge(i * 2 + 1, j * 2 + 1, abs(sr[i][2] - sr[j][2]) + abs(sr[i][3] - sr[j][3]))

        INF = int(1e18)

        def dijkstra(src: int, next_v: List[List[List[int]]]):
            dist, vis = [INF] * (nn), [False] * (nn)
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

        dis = dijkstra(n * 2, g)
        return dis[n * 2 + 1]


if __name__ == '__main__':
    # 8
    print(Solution().minimumCost([1, 1], target=[10, 4], sr=[[4, 2, 1, 1, 3], [1, 2, 7, 4, 4], [10, 3, 6, 1, 2], [6, 1, 1, 2, 3]]))
    # 5
    print(Solution().minimumCost([1, 1], target=[4, 5], sr=[[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]))
    # 7
    print(Solution().minimumCost([3, 2], target=[5, 7], sr=[[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]]))
