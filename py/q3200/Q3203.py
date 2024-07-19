"""
 * 给你两棵 无向 树，分别有 n 和 m 个节点，节点编号分别为 0 到 n - 1 和 0 到 m - 1 。
 * 给你两个二维整数数组 edges1 和 edges2 ，长度分别为 n - 1 和 m - 1 ，
 * 其中 edges1[i] = [a_i, b_i] 表示在第一棵树中节点 a_i 和 b_i 之间有一条边，
 * edges2[i] = [u_i, v_i] 表示在第二棵树中节点 u_i 和 v_i 之间有一条边。
 * 你必须在第一棵树和第二棵树中分别选一个节点，并用一条边连接它们。
 * 请你返回添加边后得到的树中，最小直径 为多少。
 * 一棵树的 直径 指的是树中任意两个节点之间的最长路径长度。
 * 提示：
 * 1、1 <= n, m <= 10^5
 * 2、edges1.length == n - 1
 * 3、edges2.length == m - 1
 * 4、edges1[i].length == edges2[i].length == 2
 * 5、edges1[i] = [a_i, b_i]
 * 6、0 <= a_i, b_i < n
 * 7、edges2[i] = [u_i, v_i]
 * 8、0 <= u_i, v_i < m
 * 9、输入保证 edges1 和 edges2 分别表示一棵合法的树。
 * 链接：https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/
"""
import math
from typing import List


class Solution:

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        n0, n1 = len(edges1) + 1, len(edges2) + 1
        nxt1, nxt2 = [[] for _ in range(n0)], [[] for _ in range(n1)]
        for u, v in edges1:
            nxt1[u].append(v)
            nxt1[v].append(u)
        for u, v in edges2:
            nxt2[u].append(v)
            nxt2[v].append(u)

        dis = 0

        def dfs(v, f, nxt):  # 获取直径
            nonlocal dis
            mx_sub = 0
            for nx in nxt[v]:
                if nx == f: continue
                sub = dfs(nx, v, nxt) + 1
                dis = max(dis, mx_sub + sub)
                mx_sub = max(sub, mx_sub)
            return mx_sub

        dfs(0, -1, nxt1)
        d0 = dis
        dis = 0
        dfs(0, -1, nxt2)
        d1 = dis
        return max(d0, d1, math.ceil(d0 / 2) + math.ceil(d1 / 2) + 1)


if __name__ == '__main__':
    # 5
    print(Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
                                               edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]))
    # 2
    print(Solution().minimumDiameterAfterMerge([[0, 1]], []))
    # 1
    print(Solution().minimumDiameterAfterMerge([], []))
    # 5
    print(Solution().minimumDiameterAfterMerge([[2, 3], [1, 5], [4, 1], [2, 6], [4, 2], [0, 7], [4, 0], [8, 4], [8, 9]],
                                               [[1, 0], [2, 1], [2, 3]]))
    # 3
    print(Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], edges2=[[0, 1]]))
