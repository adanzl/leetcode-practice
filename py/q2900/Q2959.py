"""
 * 一个公司在全国有 n 个分部，它们之间有的有道路连接。一开始，所有分部通过这些道路两两之间互相可以到达。
 * 公司意识到在分部之间旅行花费了太多时间，所以它们决定关闭一些分部（也可能不关闭任何分部），
 * 同时保证剩下的分部之间两两互相可以到达且最远距离不超过 maxDistance 。
 * 两个分部之间的 距离 是通过道路长度之和的 最小值 。
 * 给你整数 n ，maxDistance 和下标从 0 开始的二维整数数组 roads ，其中 roads[i] = [ui, vi, wi] 表示一条从 ui 到 vi 长度为 wi的 无向 道路。
 * 请你返回关闭分部的可行方案数目，满足每个方案里剩余分部之间的最远距离不超过 maxDistance。
 * 注意，关闭一个分部后，与之相连的所有道路不可通行。
 * 注意，两个分部之间可能会有多条道路。
 * 提示：
 * 1、1 <= n <= 10
 * 2、1 <= maxDistance <= 10^5
 * 3、0 <= roads.length <= 1000
 * 4、roads[i].length == 3
 * 5、0 <= ui, vi <= n - 1
 * 6、ui != vi
 * 7、1 <= wi <= 1000
 * 8、一开始所有分部之间通过道路互相可以到达。
 * 链接：https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/
"""
from math import inf
from typing import List


class Solution:

    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, wt in roads:
            g[x][y] = min(g[x][y], wt)
            g[y][x] = min(g[y][x], wt)

        f = [[]] * n

        def check(s: int) -> int:
            for i, row in enumerate(g):
                if s >> i & 1:
                    f[i] = row[:]

            # Floyd
            for k in range(n):
                if (s >> k & 1) == 0: continue
                for i in range(n):
                    if (s >> i & 1) == 0: continue
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            for i, di in enumerate(f):
                if (s >> i & 1) == 0: continue
                for j, dij in enumerate(di):
                    if s >> j & 1 and dij > maxDistance:
                        return 0
            return 1

        return sum(check(s) for s in range(1 << n))  # 枚举子集


if __name__ == '__main__':
    # 5
    print(Solution().numberOfSets(3, maxDistance=5, roads=[[0, 1, 2], [1, 2, 10], [0, 2, 10]]))
    # 7
    print(Solution().numberOfSets(3, maxDistance=5, roads=[[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]))
    # 2
    print(Solution().numberOfSets(1, maxDistance=10, roads=[]))
