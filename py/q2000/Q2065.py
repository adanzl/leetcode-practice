"""
 * 给你一张 无向 图，图中有 n 个节点，节点编号从 0 到 n - 1 （都包括）。
 * 同时给你一个下标从 0 开始的整数数组 values ，其中 values[i] 是第 i 个节点的 价值 。
 * 同时给你一个下标从 0 开始的二维整数数组 edges ，
 * 其中 edges[j] = [u_j, v_j, time_j] 表示节点 uj 和 vj 之间有一条需要 time_j 秒才能通过的无向边。
 * 最后，给你一个整数 maxTime 。
 * 合法路径 指的是图中任意一条从节点 0 开始，最终回到节点 0 ，且花费的总时间 不超过 maxTime 秒的一条路径。你可以访问一个节点任意次。
 * 一条合法路径的 价值 定义为路径中 不同节点 的价值 之和 （每个节点的价值 至多 算入价值总和中一次）。
 * 请你返回一条合法路径的 最大 价值。
 * 注意：每个节点 至多 有 四条 边与之相连。
 * 提示：
 * 1、n == values.length
 * 2、1 <= n <= 1000
 * 3、0 <= values[i] <= 10^8
 * 4、0 <= edges.length <= 2000
 * 5、edges[j].length == 3 
 * 6、0 <= u_j < v_j <= n - 1
 * 7、10 <= time_j, maxTime <= 100
 * 8、[u_j, v_j] 所有节点对 互不相同 。
 * 9、每个节点 至多有四条 边。
 * 10、图可能不连通。
 * 链接：https://leetcode.cn/problems/maximum-path-quality-of-a-graph
"""

from typing import List

#
# @lc app=leetcode.cn id=2065 lang=python3
#
# [2065] 最大化一张图中的路径价值
#


# @lc code=start
class Solution:

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v, c in edges:
            g[u].append([v, c])
            g[v].append([u, c])

        def dfs(x: int, sum_time: int, sum_value: int) -> None:
            if x == 0:
                nonlocal ans
                ans = max(ans, sum_value)
                # 注意这里没有 return，还可以继续走
            for y, t in g[x]:
                if sum_time + t > maxTime:
                    continue
                if vis[y]:
                    dfs(y, sum_time + t, sum_value)
                else:
                    vis[y] = True
                    # 每个节点的价值至多算入价值总和中一次
                    dfs(y, sum_time + t, sum_value + values[y])
                    vis[y] = False  # 恢复现场

        ans = 0
        vis = [False] * n
        vis[0] = True
        dfs(0, 0, values[0])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 75
    print(Solution().maximalPathQuality([0, 32, 10, 43], edges=[[0, 1, 10], [1, 2, 15], [0, 3, 10]], maxTime=49))
    # 25
    print(Solution().maximalPathQuality([5, 10, 15, 20], edges=[[0, 1, 10], [1, 2, 10], [0, 3, 10]], maxTime=30))
    # 7
    print(Solution().maximalPathQuality([1, 2, 3, 4],
                                        edges=[[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]],
                                        maxTime=50))
    # 0
    print(Solution().maximalPathQuality([0, 1, 2], edges=[[1, 2, 10]], maxTime=10))
