"""
 * 给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distance_i] 表示城市 ai 和 bi 之间有一条 双向 道路，
 * 道路距离为 distance_i 。城市构成的图不一定是连通的。
 * 两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。
 * 城市 1 和城市 n 之间的所有路径的 最小 分数。
 * 注意：
 * 1、一条路径指的是两个城市之间的道路序列。
 * 2、一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。
 * 3、测试数据保证城市 1 和城市n 之间 至少 有一条路径。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、1 <= roads.length <= 10^5
 * 3、roads[i].length == 3
 * 4、1 <= ai, bi <= n
 * 5、ai != bi
 * 6、1 <= distance_i <= 10^4
 * 7、不会有重复的边。
 * 8、城市 1 和城市 n 之间至少有一条路径。
 * 链接：https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/
"""
from typing import List


class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        INF = 0x3c3c3c3c
        parent = [i for i in range(n)]
        vals = [INF] * n

        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]

        for s, e, c in roads:
            r1, r2 = find(s - 1), find(e - 1)
            mn = min(vals[r1], vals[r2], c)
            vals[r1] = vals[r2] = mn
            parent[r1] = parent[r2]
        return vals[find(0)]


if __name__ == '__main__':
    # 5
    print(Solution().minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
    # 2
    print(Solution().minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
