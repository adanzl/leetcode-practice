"""
 * 给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。
 * 给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。
 * 同时给你一个二维数组 edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。
 * 图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图中有一条有向边。
 * 路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。
 * 请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。
 * 提示：
 * 1、n == colors.length
 * 2、m == edges.length
 * 3、1 <= n <= 10^5
 * 4、0 <= m <= 10^5
 * 5、colors 只含有小写英文字母。
 * 6、0 <= aj, bj < n
 * 链接：https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/
"""
from collections import Counter
from typing import List


class Solution:

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        front = [0] * n
        dp = [Counter() for _ in range(n)]
        for i in range(n):
            dp[i][colors[i]] = 1
        q = set(range(n))
        for s, e in edges:
            g[s].append(e)
            front[e] += 1
            q.discard(e)
        ans = 1
        cnt = len(q)
        while q:
            t = q
            q = []
            for idx in t:
                for nx in g[idx]:
                    for c, v in dp[idx].items():
                        dp[nx][c] = max(dp[nx][c], v + (1 if c == colors[nx] else 0))
                        ans = max(ans, dp[nx][c])
                    front[nx] -= 1
                    if front[nx] == 0:
                        q.append(nx)
                        cnt += 1
        if cnt < n: return -1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().largestPathValue("abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
    # -1
    print(Solution().largestPathValue("a", edges=[[0, 0]]))