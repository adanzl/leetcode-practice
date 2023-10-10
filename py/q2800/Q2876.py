"""
 * 现有一个有向图，其中包含 n 个节点，节点编号从 0 到 n - 1 。此外，该图还包含了 n 条有向边。
 * 给你一个下标从 0 开始的数组 edges ，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的边。
 * 想象在图上发生以下过程：
 * 你从节点 x 开始，通过边访问其他节点，直到你在 此过程 中再次访问到之前已经访问过的节点。
 * 返回数组 answer 作为答案，其中 answer[i] 表示如果从节点 i 开始执行该过程，你可以访问到的不同节点数。
 * 提示：
 * 1、n == edges.length
 * 2、2 <= n <= 10^5
 * 3、0 <= edges[i] <= n - 1
 * 4、edges[i] != i
 * 链接：https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/
"""
from typing import List


class Solution:

    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        # 删除孤立的边
        in_d = [0] * n
        for i, e in enumerate(edges):
            in_d[e] += 1
        q = [i for i in range(n) if in_d[i] == 0]
        d, cnt = 0, 0
        while q:
            t = []
            for cur in q:
                cnt += 1
                ans[cur] = d + 1
                nx = edges[cur]
                in_d[nx] -= 1
                if in_d[nx] == 0:
                    t.append(nx)
            q = t
            d += 1
        # 计算环长
        c_idx = 1
        c_len = {}
        c_map = [0] * n  # circle idx map
        for i in [v for v in range(n) if ans[v] == 0]:
            if c_map[i] != 0: continue
            p, c_l = i, 0
            while c_map[p] == 0:
                c_l += 1
                c_map[p] = c_idx
                p = edges[p]
            c_len[c_idx] = c_l
            c_idx += 1
        # 计算孤立的边长
        for i in [v for v in range(n) if ans[v] == 1]:
            if ans[i] == 0: continue
            nn = i
            s = [nn]
            while ans[nn] != 0:
                s.append(nn)
                nn = edges[nn]
            for ii, e in enumerate(s):
                ans[e] = len(s) - ii + c_len[c_map[nn]]
        for i in [v for v in range(n) if c_map[v] != 0]:
            ans[i] = c_len[c_map[i]]
        # print(cnt, ans)
        return ans


if __name__ == '__main__':
    # [2,2,3,2,3,4,2,3,3]
    print(Solution().countVisitedNodes([6, 3, 6, 1, 0, 8, 0, 6, 6]))
    # [2,3,3,3,5,4,4,2]
    print(Solution().countVisitedNodes([7, 0, 7, 0, 5, 3, 3, 0]))
    # [2, 7, 8, 2, 5, 4, 6, 3]
    print(Solution().countVisitedNodes([3, 6, 1, 0, 5, 7, 4, 3]))
    # [3,3,3,4]
    print(Solution().countVisitedNodes([1, 2, 0, 0]))
    # [5,5,5,5,5]
    print(Solution().countVisitedNodes([1, 2, 3, 4, 0]))