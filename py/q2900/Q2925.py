"""
 * 有一棵 n 个节点的无向树，节点编号为 0 到 n - 1 ，根节点编号为 0 。
 * 给你一个长度为 n - 1 的二维整数数组 edges 表示这棵树，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 有一条边。
 * 同时给你一个长度为 n 下标从 0 开始的整数数组 values ，其中 values[i] 表示第 i 个节点的值。
 * 一开始你的分数为 0 ，每次操作中，你将执行：
 * 1、选择节点 i 。
 * 2、将 values[i] 加入你的分数。
 * 3、将 values[i] 变为 0 。
 * 如果从根节点出发，到任意叶子节点经过的路径上的节点值之和都不等于 0 ，那么我们称这棵树是 健康的 。
 * 你可以对这棵树执行任意次操作，但要求执行完所有操作以后树是 健康的 ，请你返回你可以获得的 最大分数 。
 * 提示：
 * 1、2 <= n <= 2 * 10^4
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、values.length == n
 * 6、1 <= values[i] <= 10^9
 * 7、输入保证 edges 构成一棵合法的树。
 * 链接：https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/
"""
from functools import cache
from typing import List


class Solution:

    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def dfs(u, fa, zero):
            if u and len(g[u]) == 1:
                return values[u] if not zero else 0
            ret0, ret1 = values[u], 0
            for nx in g[u]:
                if nx == fa: continue
                ret0 += dfs(nx, u, zero)
                ret1 += dfs(nx, u, False)
            return max(ret0, ret1)

        return dfs(0, -1, True)


if __name__ == '__main__':
    # 11
    print(Solution().maximumScoreAfterOperations([[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values=[5, 2, 5, 2, 1, 1]))
    # 40
    print(Solution().maximumScoreAfterOperations([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[20, 10, 9, 7, 4, 3, 5]))
