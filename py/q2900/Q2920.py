"""
 * 节点 0 处现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 。
 * 给你一个长度为 n - 1 的二维 整数 数组 edges ，其中 edges[i] = [ai, bi] 表示在树上的节点 ai 和 bi 之间存在一条边。
 * 另给你一个下标从 0 开始、长度为 n 的数组 coins 和一个整数 k ，其中 coins[i] 表示节点 i 处的金币数量。
 * 从根节点开始，你必须收集所有金币。要想收集节点上的金币，必须先收集该节点的祖先节点上的金币。
 * 节点 i 上的金币可以用下述方法之一进行收集：
 * 1、收集所有金币，得到共计 coins[i] - k 点积分。如果 coins[i] - k 是负数，你将会失去 abs(coins[i] - k) 点积分。
 * 2、收集所有金币，得到共计 floor(coins[i] / 2) 点积分。
 *    如果采用这种方法，节点 i 子树中所有节点 j 的金币数 coins[j] 将会减少至 floor(coins[j] / 2) 。
 * 返回收集 所有 树节点的金币之后可以获得的最大积分。
 * 提示：
 * 1、n == coins.length
 * 2、2 <= n <= 10^5
 * 3、0 <= coins[i] <= 10^4
 * 4、edges.length == n - 1
 * 5、0 <= edges[i][0], edges[i][1] < n
 * 6、0 <= k <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes
"""
from functools import cache
import sys
from typing import List

sys.setrecursionlimit(2 * 10**5)


class Solution:

    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)

        @cache
        def dfs(u, fa, f):
            if f > 13: return 0
            v0, v1 = (coins[u] >> f) - k, coins[u] >> (f + 1)
            for nx in g[u]:
                if nx == fa: continue
                v0 += dfs(nx, u, f)
                v1 += dfs(nx, u, f + 1)
            return max(v0, v1)

        return dfs(0, -1, 0)


if __name__ == '__main__':
    # 8
    print(Solution().maximumPoints([[0, 1], [0, 2], [3, 2], [0, 4]], [5, 6, 8, 7, 4], k=7))
    # 10
    print(Solution().maximumPoints([[0, 1], [2, 0], [0, 3], [4, 2]], [7, 5, 0, 9, 3], 4))
    # 11
    print(Solution().maximumPoints([[0, 1], [1, 2], [2, 3]], coins=[10, 10, 3, 3], k=5))
    # 16
    print(Solution().maximumPoints([[0, 1], [0, 2]], coins=[8, 4, 4], k=0))
