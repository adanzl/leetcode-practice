"""
 * 给你一个 n 个点的无向图，节点从 0 到 n - 1 编号。给你一个长度为 n 下标从 0 开始的整数数组 vals ，其中 vals[i] 表示第 i 个节点的值。
 * 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条双向边。
 * 星图 是给定图中的一个子图，它包含一个中心节点和 0 个或更多个邻居。换言之，星图是给定图中一个边的子集，且这些边都有一个公共节点。
 * 下图分别展示了有 3 个和 4 个邻居的星图，蓝色节点为中心节点。
 * 星和 定义为星图中所有节点值的和。
 * 给你一个整数 k ，请你返回 至多 包含 k 条边的星图中的 最大星和 。
 * 提示：
 * 1、n == vals.length
 * 2、1 <= n <= 10^5
 * 3、-10^4 <= vals[i] <= 10^4
 * 4、0 <= edges.length <= min(n * (n - 1) / 2, 10^5)
 * 5、edges[i].length == 2
 * 6、0 <= ai, bi <= n - 1
 * 7、ai != bi
 * 8、0 <= k <= n - 1
 * 链接：https://leetcode.cn/problems/maximum-star-sum-of-a-graph/
"""
from typing import List


class Solution:

    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for s, e in edges:
            g[s].append(vals[e])
            g[e].append(vals[s])
        ans = -0x3c3c3c3c
        for i in range(n):
            g[i].sort(reverse=True)
            sm = vals[i]
            for j, v in enumerate(g[i]):
                if v < 0 or j >= k: break
                sm += v
            ans = max(ans, sm)
        return ans


if __name__ == '__main__':
    # 16
    print(Solution().maxStarSum([1, 2, 3, 4, 10, -10, -20], [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]], 2))
    # -5
    print(Solution().maxStarSum([-5], [], 0))
