"""
 * 给你一棵 无向 树，树中节点从 0 到 n - 1 编号。同时给你一个长度为 n - 1 的二维整数数组 edges ，
 * 其中 edges[i] = [u_i, v_i] 表示节点 u_i 和 v_i 在树中有一条边。
 * 一开始，所有 节点都 未标记 。对于节点 i ：
 * 1、当 i 是奇数时，如果时刻 x - 1 该节点有 至少 一个相邻节点已经被标记了，那么节点 i 会在时刻 x 被标记。
 * 2、当 i 是偶数时，如果时刻 x - 2 该节点有 至少 一个相邻节点已经被标记了，那么节点 i 会在时刻 x 被标记。
 * 请你返回一个数组 times ，表示如果你在时刻 t = 0 标记节点 i ，那么时刻 times[i] 时，树中所有节点都会被标记。
 * 请注意，每个 times[i] 的答案都是独立的，即当你标记节点 i 时，所有其他节点都未标记。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= edges[i][0], edges[i][1] <= n - 1
 * 5、输入保证 edges 表示一棵合法的树。
 * 链接：https://leetcode.cn/problems/time-taken-to-mark-all-nodes/
"""
from typing import List


class Solution:

    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        # 换根dp 树上拓扑
        f = [0] * n  # 0-i
        dp = [0] * n  # i-0

        def dfs(idx, fa):
            for nx in g[idx]:
                if nx == fa: continue
                dfs(nx, idx)
                f[idx] = max(f[idx], (1 if nx & 1 else 2) + f[nx])

        def dfs_reverse(idx, fa):
            mx, mx_nx = -1, -1  # 最大成本子节点
            s_mx = -1  # 次大成本子节点
            for nx in g[idx]:
                if nx == fa: continue
                t = (f[nx] + 1) if (nx & 1) else (f[nx] + 2)
                if t > mx:
                    s_mx = mx
                    mx, mx_nx = t, nx
                elif t > s_mx:
                    s_mx = t
            tu = 1 if (idx & 1) else 2
            for nx in g[idx]:
                if nx == fa: continue
                if nx == mx_nx:
                    dp[nx] = max(dp[nx], max(dp[idx], s_mx) + tu)
                else:
                    dp[nx] = max(dp[nx], max(dp[idx], mx) + tu)
                dfs_reverse(nx, idx)

        dfs(0, -1)
        dfs_reverse(0, -1)
        return [max(dp[i], f[i]) for i in range(n)]


if __name__ == '__main__':
    # [2,4,3]
    print(Solution().timeTaken([[0, 1], [0, 2]]))
    # [1,2]
    print(Solution().timeTaken([[0, 1]]))
    # [4,6,3,5,5]
    print(Solution().timeTaken([[2, 4], [0, 1], [2, 3], [0, 2]]))
