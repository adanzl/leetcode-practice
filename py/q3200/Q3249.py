"""
 * 现有一棵 无向 树，树中包含 n 个节点，按从 0 到 n - 1 标记。树的根节点是节点 0 。
 * 给你一个长度为 n - 1 的二维整数数组 edges，其中 edges[i] = [a_i, b_i] 表示树中节点 a_i 与节点 b_i 之间存在一条边。
 * 如果一个节点的所有子节点为根的 子树 包含的节点数相同，则认为该节点是一个 好节点。
 * 返回给定树中 好节点 的数量。
 * 子树 指的是一个节点以及它所有后代节点构成的一棵树。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= a_i, b_i < n
 * 5、输入确保 edges 总表示一棵有效的树。
 * 链接：https://leetcode.cn/problems/count-the-number-of-good-nodes/description/
"""
from typing import List


class Solution:

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        ans = 0
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)

        def dfs(idx, fa):
            ret = 0  # depth
            nonlocal ans
            sub = -1
            valid = True
            for nx in g[idx]:
                if nx == fa: continue
                s = dfs(nx, idx)
                if s != sub:
                    if sub != -1:
                        valid = False
                    sub = s
                ret += s
            if valid:
                ans += 1
            return ret + 1

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().countGoodNodes([[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]))
    # 7
    print(Solution().countGoodNodes([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
    # 12
    print(Solution().countGoodNodes([[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10],
                                     [9, 12], [10, 11]]))
