"""
 * 小明的电动车电量充满时可行驶距离为 cnt，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间。小明想选择电动车作为代步工具。
 * 地图上共有 N 个景点，景点编号为 0 ~ N-1。他将地图信息以 [城市 A 编号,城市 B 编号,两城市间距离] 格式整理在在二维数组 paths，表示城市 A、B 间存在双向通路。
 * 初始状态，电动车电量为 0。每个城市都设有充电桩，charge[i] 表示第 i 个城市每充 1 单位电量需要花费的单位时间。
 * 请返回小明最少需要花费多少单位时间从起点城市 start 抵达终点城市 end。
 * 提示：
 * 1、1 <= paths.length <= 200
 * 2、paths[i].length == 3
 * 3、2 <= charge.length == n <= 100
 * 4、0 <= path[i][0],path[i][1],start,end < n
 * 5、1 <= cnt <= 100
 * 6、1 <= path[i][2] <= cnt
 * 7、1 <= charge[i] <= 100
 * 8、题目保证所有城市相互可以到达
 * 链接：https://leetcode.cn/problems/DFPeFJ/
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:

    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        inf = int(1e18)
        n = len(charge)
        g = [[] for _ in range(n)]
        dis = defaultdict(lambda: inf)
        # 分层图、dijkstra、将“{idx(城市)，cap(在该城市出发时的电量)}” 视为图的节点
        # 初步建图的时候使用 城市-距离
        for s, e, c in paths:
            g[s].append([e, c])
            g[e].append([s, c])
        q = [[0, 0, start]]  # time-cap-idx 最小时间-电量-城市
        while q:
            t, c, idx = heappop(q)
            if (idx, 0) == (end, 0): return t
            if (idx, c) in dis: continue
            dis[(idx, c)] = t
            # 不充电能跑到哪，相当于在同一层
            for nx_i, nx_c in g[idx]:  # 城市-距离
                if c < nx_c: continue
                if (nx_i, c - nx_c) not in dis:
                    heappush(q, [t + nx_c, c - nx_c, nx_i])
            # 此处将图分层, 如果还能充电则进入下一层
            if c < cnt:
                heappush(q, [t + charge[idx], c + 1, idx])
        return -1


if __name__ == '__main__':
    # 699
    print(Solution().electricCarPlan([[0, 2, 4], [0, 1, 18], [7, 2, 18], [0, 6, 17], [8, 0, 82], [1, 6, 10], [1, 3, 10], [0, 3, 72], [2, 8, 70], [4, 5, 77], [0, 5, 58], [0, 8, 32], [7, 6, 85],
                                      [3, 7, 51], [5, 4, 53], [5, 3, 12], [7, 8, 61], [5, 3, 1], [1, 3, 39], [3, 2, 10], [1, 6, 32], [0, 4, 82], [5, 3, 81], [1, 2, 62]], 92, 3, 7,
                                     [24, 82, 19, 63, 2, 24, 46, 32, 27]))
    # 3801
    print(Solution().electricCarPlan([[3, 7, 32], [0, 6, 46], [1, 0, 47], [0, 6, 8], [0, 3, 30], [1, 5, 34], [1, 2, 9], [1, 4, 29], [0, 1, 6]], 52, 4, 5, [90, 57, 24, 52, 75, 61, 39, 20]))
    # 43
    print(Solution().electricCarPlan([[1, 3, 3], [3, 2, 1], [2, 1, 3], [0, 1, 4], [3, 0, 5]], 6, 1, 0, [2, 10, 4, 1]))
    # 38
    print(Solution().electricCarPlan([[0, 4, 2], [4, 3, 5], [3, 0, 5], [0, 1, 5], [3, 2, 4], [1, 2, 8]], 8, 0, 2, [4, 1, 1, 3, 2]))
