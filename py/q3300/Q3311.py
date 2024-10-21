"""
 * 给你一个二维整数数组 edges ，它表示一棵 n 个节点的 无向 图，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 之间有一条边。
 * 请你构造一个二维矩阵，满足以下条件：
 * 1、矩阵中每个格子 一一对应 图中 0 到 n - 1 的所有节点。
 * 2、矩阵中两个格子相邻（横 的或者 竖 的）当且仅当 它们对应的节点在 edges 中有边连接。
 * 题目保证 edges 可以构造一个满足上述条件的二维矩阵。
 * 请你返回一个符合上述要求的二维整数数组，如果存在多种答案，返回任意一个。
 * 提示：
 * 1、2 <= n <= 5 * 10^4
 * 2、1 <= edges.length <= 10^5
 * 3、edges[i] = [ui, vi]
 * 4、0 <= ui < vi < n
 * 5、树中的边互不相同。
 * 6、输入保证 edges 可以形成一个符合上述条件的二维矩阵。
 * 链接：https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/description/
"""

from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=3311 lang=python3
# @lcpr version=20000
#
# [3311] 构造符合图结构的二维矩阵
#


# @lc code=start
class Solution:

    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [set() for _ in range(n)]
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        ans = [[]]
        p = -1
        for i in range(n):
            if p == -1 or len(g[i]) < len(g[p]):
                p = i
        vis = set([p])
        pq = [[] for _ in range(n)]
        arr = [p]
        ii = 0
        while arr:
            n_arr = []
            vis_line = set()
            if len(pq[arr[0]]) == 1:
                ans.append([])
            for i, u in enumerate(arr):
                ans[ii - i].append(u)
                vis.add(u)
                for nx in g[u]:
                    if nx in vis: continue
                    if nx not in vis_line:
                        vis_line.add(nx)
                        n_arr.append(nx)
                    pq[nx].append(i)
            n_arr.sort(key=lambda x: pq[x])
            arr = n_arr
            if n_arr and len(pq[n_arr[0]]) == 1:
                ii += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # [[3,1],[2,0]]
    print(Solution().constructGridLayout(9,
                                         edges=[[0, 1], [0, 4], [0, 5], [1, 7], [2, 3], [2, 4], [2, 5], [3, 6], [4, 6],
                                                [4, 7], [6, 8], [7, 8]]))
    # [[8,6,3],[7,4,2],[1,0,5]]
    print(Solution().constructGridLayout(4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]]))
    # [[4,2,3,1,0]]
    print(Solution().constructGridLayout(5, edges=[[0, 1], [1, 3], [2, 3], [2, 4]]))
