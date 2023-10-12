"""
 * 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
 * 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
 * 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
 * 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
 * 提示：
 * 1、1 <= routes.length <= 500.
 * 2、1 <= routes[i].length <= 10^5
 * 3、routes[i] 中的所有值 互不相同
 * 4、sum(routes[i].length) <= 10^5
 * 5、0 <= routes[i][j] < 10^6
 * 6、0 <= source, target < 10^6
 * 链接：https://leetcode.com/problems/bus-routes/description/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#


# @lc code=start
class Solution:

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n_l = len(routes)
        station = defaultdict(set)  # station belong line idx

        for i, r in enumerate(routes):
            for s in r:
                station[s].add(i)
        if station[source] & station[target]:
            return 1
        q = []  # line
        vis = [False] * n_l  # line
        for s in station[source]:
            q.append(s)
            vis[s] = True
        d = 1
        while q:
            t = []
            for line in q:
                for s in routes[line]:
                    for nx_l in station[s]:
                        if vis[nx_l]: continue
                        if nx_l in station[target]:
                            return d + 1
                        vis[nx_l] = True
                        t.append(nx_l)
            q = t
            d += 1

        return -1


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().numBusesToDestination([[2], [2, 8]], 8, 2))
    # 2
    print(Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], source=1, target=6))
    # -1
    print(Solution().numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12))