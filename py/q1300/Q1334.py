"""
 * 有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [from_i, to_i, weight_i] 代表 from_i 和 to_i 两个城市之间的双向加权边，
 * 距离阈值是一个整数 distanceThreshold。
 * 返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。
 * 注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。
 * 提示：
 * 1、2 <= n <= 100
 * 2、1 <= edges.length <= n * (n - 1) / 2
 * 3、edges[i].length == 3
 * 4、0 <= from_i < to_i < n
 * 5、1 <= weight_i, distanceThreshold <= 10^4
 * 6、所有 (from_i, to_i) 都是不同的。
 * 链接：https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""
from typing import List


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = 0x3c3c3c3c
        min = lambda a, b: a if a < b else b
        dis = [[0 if i == j else inf for i in range(n)] for j in range(n)]
        for f, t, v in edges:
            dis[f][t] = dis[t][f] = v
        ans, count = 0, n + 1
        # Floyed
        for k in range(n):  # 遍历中间节点，此处必须放在最外层
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        for i in range(n):
            cur = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    cur +=1
            if cur <= count:
                ans, count = i, cur
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
    # 0
    print(Solution().findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))
