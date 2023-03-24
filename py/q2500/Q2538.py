"""
 * 给你一个 n 个节点的无向无根图，节点编号为 0 到 n - 1 。
 * 给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
 * 每个节点都有一个价值。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价值。
 * 一条路径的 价值和 是这条路径上所有节点的价值之和。
 * 你可以选择树中任意一个节点作为根节点 root 。选择 root 为根的 开销 是以 root 为起点的所有路径中，价值和 最大的一条路径与最小的一条路径的差值。
 * 请你返回所有节点作为根节点的选择中，最大 的 开销 为多少。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、0 <= ai, bi <= n - 1
 * 4、edges 表示一棵符合题面要求的树。
 * 5、price.length == n
 * 6、1 <= price[i] <= 10^5
 * 链接：https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/
"""
from functools import cache
from typing import List


class Solution:

    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def dfs(idx, par):
            ans = price[idx]
            for v in g[idx]:
                if v != par:
                    ans = max(ans, dfs(v, idx) + price[idx])
            return ans

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i, -1) - price[i])
        return ans


if __name__ == '__main__':
    # 24
    print(Solution().maxOutput(6, edges=[[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], price=[9, 8, 7, 6, 10, 5]))
    # 2
    print(Solution().maxOutput(3, edges=[[0, 1], [1, 2]], price=[1, 1, 1]))
