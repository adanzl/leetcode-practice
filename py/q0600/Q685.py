"""
 * 在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。
 * 该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
 * 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。
 * 附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
 * 结果图是一个以边组成的二维数组 edges 。 
 * 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。
 * 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
 * 提示：
 * 1、n == edges.length
 * 2、3 <= n <= 1000
 * 3、edges[i].length == 2
 * 4、1 <= ui, vi <= n
 * 链接：https://leetcode.cn/problems/redundant-connection-ii/
"""

from typing import List

#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#


# @lc code=start
class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        def find(x, fa):
            if x == fa[x]: return x
            fa[x] = find(fa[x], fa)
            return fa[x]

        def union(skip_i):
            cnt = n
            fa = list(range(n))
            for j in range(n):
                if skip_i == j: continue
                u, v = edges[j][0] - 1, edges[j][1] - 1
                ru, rv = find(u, fa), find(v, fa)
                if ru != rv:
                    cnt -= 1
                    fa[rv] = ru
            return cnt

        in_d = [-1] * n
        for i, (u, v) in enumerate(edges):
            if in_d[v - 1] != -1:  # 入度大于1
                for j in [i, in_d[v - 1]]:
                    cnt = union(j)
                    if cnt == 1:
                        return edges[j]
            in_d[v - 1] = i
        # 没有根
        for i in range(n - 1, -1, -1):
            cnt = union(i)
            if cnt == 1:
                return edges[i]
        return []


# @lc code=end

if __name__ == '__main__':
    # [2,1]
    print(Solution().findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]))
    # [4,1]
    print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
    # [2,3]
    print(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
