"""
 * 给你一棵 n 个节点的树（连通无向无环的图），节点编号从 0 到 n - 1 且恰好有 n - 1 条边。
 * 给你一个长度为 n 下标从 0 开始的整数数组 vals ，分别表示每个节点的值。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
 * 一条 好路径 需要满足以下条件：
 * 1、开始节点和结束节点的值 相同 。
 * 2、开始节点和结束节点中间的所有节点值都 小于等于 开始节点的值（也就是说开始节点的值应该是路径上所有节点的最大值）。
 * 请你返回不同好路径的数目。
 * 注意，一条路径和它反向的路径算作 同一 路径。比方说， 0 -> 1 与 1 -> 0 视为同一条路径。单个节点也视为一条合法路径。
 * 提示：
 * 1、n == vals.length
 * 2、1 <= n <= 3 * 10^4
 * 3、0 <= vals[i] <= 10^5
 * 4、edges.length == n - 1
 * 5、edges[i].length == 2
 * 6、0 <= ai, bi < n
 * 7、ai != bi
 * 8、edges 表示一棵合法的树。
 * 链接：https://leetcode.cn/problems/number-of-good-paths/
"""

from typing import *


class Solution:

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        parent = list(range(n))

        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        size = [1] * n
        ans = n
        for v, i in sorted(zip(vals, range(n))):
            rx = find(i)
            for next in g[i]:
                ry = find(next)
                if vals[ry] > v or ry == rx:
                    continue
                if vals[ry] == v:
                    ans += size[ry] * size[rx]
                    size[rx] += size[ry]
                parent[ry] = rx
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().numberOfGoodPaths([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]))
    # 7
    print(Solution().numberOfGoodPaths([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]))
