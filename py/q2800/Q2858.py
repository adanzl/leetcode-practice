"""
 * 给你一个 n 个点的 简单有向图 （没有重复边的有向图），节点编号为 0 到 n - 1 。如果这些边是双向边，那么这个图形成一棵 树 。
 * 给你一个整数 n 和一个 二维 整数数组 edges ，其中 edges[i] = [ui, vi] 表示从节点 ui 到节点 vi 有一条 有向边 。
 * 边反转 指的是将一条边的方向反转，也就是说一条从节点 ui 到节点 vi 的边会变为一条从节点 vi 到节点 ui 的边。
 * 对于范围 [0, n - 1] 中的每一个节点 i ，你的任务是分别 独立 计算 最少 需要多少次 边反转 ，从节点 i 出发经过 一系列有向边 ，可以到达所有的节点。
 * 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]表示从节点 i 出发，可以到达所有节点的 最少边反转 次数。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ui == edges[i][0] < n
 * 5、0 <= vi == edges[i][1] < n
 * 6、ui != vi
 * 7、输入保证如果边是双向边，可以得到一棵树。
 * 链接：https://leetcode.cn/problems/minimum-edge-reversals-so-every-node-is-reachable/
"""
from functools import cache
from typing import List


class Solution:

    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # 换根dp解法
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append((y, 1))
            g[y].append((x, -1))  # 从 y 到 x 需要反向

        ans = [0] * n

        def dfs(x: int, fa: int) -> None:
            for y, dir in g[x]:
                if y == fa: continue
                # ！！！ 关键替换代码
                ans[0] += dir < 0
                dfs(y, x)

        dfs(0, -1)

        def re_root(x: int, fa: int) -> None:
            for y, dir in g[x]:
                if y == fa: continue
                # ！！！ 关键替换代码
                ans[y] = ans[x] + dir  # dir 就是从 x 换到 y 的「变化量」
                re_root(y, x)

        re_root(0, -1)
        return ans

    def minEdgeReversals1(self, n: int, edges: List[List[int]]) -> List[int]:
        nxt = [[] for _ in range(n)]
        pre = [[] for _ in range(n)]
        for u, v in edges:
            nxt[u].append(v)
            pre[v].append(u)

        @cache
        def dfs(i, fa):
            ret = 0
            for nx in nxt[i]:
                if nx == fa: continue
                ret += dfs(nx, i)
            for pr in pre[i]:
                if pr == fa: continue
                ret += dfs(pr, i) + 1
            return ret

        return [dfs(i, -1) for i in range(n)]


if __name__ == '__main__':
    # [1,1,0,2]
    print(Solution().minEdgeReversals(4, [[2, 0], [2, 1], [1, 3]]))
    # [2,0,1]
    print(Solution().minEdgeReversals(3, edges=[[1, 2], [2, 0]]))
    #
    # print(Solution().minEdgeReversals())