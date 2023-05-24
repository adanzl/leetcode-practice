"""
 * 给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：
 * 1、在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
 * 2、青蛙无法跳回已经访问过的顶点。
 * 3、如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
 * 4、如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
 * 无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。
 * 返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10-5 的结果将被视为正确答案。
 * 提示：
 * 1、1 <= n <= 100
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、1 <= ai, bi <= n
 * 5、1 <= t <= 50
 * 6、1 <= target <= n
 * 链接：https://leetcode.cn/problems/frog-position-after-t-seconds/
"""
from typing import List


class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        ans = [0.0] * (n + 1)
        ans[1] = 1.0
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = [[1, -1]]
        for _ in range(t):
            tt = []
            for idx, fa in q:
                ss = len(g[idx]) - 1 if fa != -1 else len(g[idx])
                pre_v = ans[idx]
                for nx in g[idx]:
                    if nx == fa: continue
                    ans[nx] = pre_v / ss
                    ans[idx] = 0
                    tt.append([nx, idx])
            q = tt
            if not q: break
        return ans[target]


if __name__ == '__main__':
    # 0.00000
    print(Solution().frogPosition(8, [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], 7, 7))
    # 0.16666666666666666
    print(Solution().frogPosition(7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))
    # 0.3333333333333333
    print(Solution().frogPosition(7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
