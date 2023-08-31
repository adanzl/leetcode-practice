"""
 * 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。
 * 一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。
 * 连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。
 * 请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。
 * 提示：
 * 1、2 <= n <= 400
 * 2、edges[i].length == 2
 * 3、1 <= edges.length <= n * (n-1) / 2
 * 4、1 <= ui, vi <= n
 * 5、ui != vi
 * 6、图中没有重复的边。
 * 链接：https://leetcode.cn/problems/minimum-degree-of-a-connected-trio-in-a-graph
"""

from typing import List

#
# @lc app=leetcode.cn id=1761 lang=python3
#
# [1761] 一个图中连通三元组的最小度数
#


# @lc code=start
class Solution:

    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        grid = [[0] * (n) for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            grid[u - 1][v - 1] = grid[v - 1][u - 1] = 1
            deg[u - 1] += 1
            deg[v - 1] += 1
        INF = 10**10
        ans = INF
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if grid[i][j] and grid[j][k] and grid[k][i]:
                        ans = min(ans, deg[i] + deg[j] + deg[k] - 6)
        return ans if ans != INF else -1


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().minTrioDegree(6, edges=[[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]))
    # 0
    print(Solution().minTrioDegree(7, edges=[[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]))