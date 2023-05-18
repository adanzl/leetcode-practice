"""
 * 给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] = [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。
 * 返回图中 完全连通分量 的数量。
 * 如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
 * 如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。
 * 提示：
 * 1、1 <= n <= 50
 * 2、0 <= edges.length <= n * (n - 1) / 2
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi <= n - 1
 * 5、ai != bi
 * 6、不存在重复的边
 * 链接：https://leetcode.cn/problems/count-the-number-of-complete-components/
"""
from typing import List


class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [[i, 1] for i in range(n)]

        def find(x: int):
            if parent[x][0] != x:
                parent[x][0] = find(parent[x][0])
            return parent[x][0]

        for u, v in edges:
            if v < u: v, u = u, v
            r1, r2 = find(u), find(v)
            if r1 != r2:
                parent[r2][1] += parent[r1][1]
                parent[r1] = parent[r2]
        cnt = [0] * n
        ans = 0
        for u, v in edges:
            if v < u: v, u = u, v
            cnt[find(u)] += 1
        for i in range(n):
            nn = parent[find(i)][1]
            if nn == 0: continue
            if cnt[i] == nn * (nn - 1) // 2:
                ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countCompleteComponents(6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
    # 1
    print(Solution().countCompleteComponents(6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
