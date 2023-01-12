"""
 * 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。
 * 你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。
 * 无向树的边由 edges 给出，其中 edges[i] = [from_i, to_i] ，表示有一条边连接 from_i 和 to_i 。
 * 除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、edges.length == n-1
 * 3、edges[i].length == 2
 * 4、0 <= from_i, to_i <= n-1
 * 5、from_i < to_i
 * 6、hasApple.length == n
 * 链接：https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""
from typing import List


class Solution:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for s, e in edges:
            g[s].append(e)
            g[e].append(s)

        def dfs(idx, vis):
            d, apple = 0, hasApple[idx]
            for nx in g[idx]:
                if nx in vis: continue
                vis.add(nx)
                r, a = dfs(nx, vis)
                apple |= a
                if a: d += r + 2
            return d, apple

        return dfs(0, set([0]))[0]


if __name__ == '__main__':
    # 8
    print(Solution().minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]))
    # 6
    print(Solution().minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]))
    # 0
    print(Solution().minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]))
