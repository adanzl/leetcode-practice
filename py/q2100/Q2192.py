"""
 * 给你一个正整数 n ，它表示一个 有向无环图 中节点的数目，节点编号为 0 到 n - 1 （包括两者）。
 * 给你一个二维整数数组 edges ，其中 edges[i] = [from_i, to_i] 表示图中一条从 from_i 到 to_i 的单向边。
 * 请你返回一个数组 answer，其中 answer[i]是第 i 个节点的所有 祖先 ，这些祖先节点 升序 排序。
 * 如果 u 通过一系列边，能够到达 v ，那么我们称节点 u 是节点 v 的 祖先 节点。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、0 <= edges.length <= min(2000, n * (n - 1) / 2)
 * 3、edges[i].length == 2
 * 4、0 <= from_i, to_i <= n - 1
 * 5、from_i != to_i
 * 6、图中不会有重边。
 * 7、图是 有向 且 无环 的。
 * 链接：https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph
"""

from functools import cache
from typing import Deque, List

#
# @lc app=leetcode.cn id=2192 lang=python3
#
# [2192] 有向无环图中一个节点的所有祖先
#


# @lc code=start
class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        pre = [[] for _ in range(n)]
        o_d = [0] * n
        for u, v in edges:
            pre[v].append(u)
            o_d[u] += 1
        ans = [set() for _ in range(n)]

        @cache
        def dfs(idx):
            ret = set()
            for pr in pre[idx]:
                ret.add(pr)
                ret.update(dfs(pr))
            return ret

        for i in range(n):
            ans[i] = dfs(i)
        return [sorted(v) for v in ans]


# @lc code=end

if __name__ == '__main__':
    # [[2,4,5],[0,2,4,5],[4],[0,1,2,4,5],[],[2,4]]
    print(Solution().getAncestors(
        6, [[0, 3], [5, 0], [2, 3], [4, 3], [5, 3], [1, 3], [2, 5], [0, 1], [4, 5], [4, 2], [4, 0], [2, 1], [5, 1]]))
    # [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    print(Solution().getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
    # [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    print(Solution().getAncestors(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
