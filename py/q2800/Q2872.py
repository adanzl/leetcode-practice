"""
 * 给你一棵 n 个节点的无向树，节点编号为 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，
 * 其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 有一条边。
 * 同时给你一个下标从 0 开始长度为 n 的整数数组 values ，其中 values[i] 是第 i 个节点的 值 。再给你一个整数 k 。
 * 你可以从树中删除一些边，也可以一条边也不删，得到若干连通块。一个 连通块的值 定义为连通块中所有节点值之和。
 * 如果所有连通块的值都可以被 k 整除，那么我们说这是一个 合法分割 。
 * 请你返回所有合法分割中，连通块数目的最大值 。
 * 提示：
 * 1、1 <= n <= 3 * 10^4
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、values.length == n
 * 6、0 <= values[i] <= 10^9
 * 7、1 <= k <= 10^9
 * 8、values 之和可以被 k 整除。
 * 9、输入保证 edges 是一棵无向树。
 * 链接：https://leetcode.cn/problems/maximum-number-of-k-divisible-components/
"""
from typing import List


class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)
        ans = 0

        def dfs(node, fa):
            nonlocal ans
            ret = values[node]
            for nx in g[node]:
                if nx == fa: continue
                sub = dfs(nx, node)
                ret += sub
            if ret % k == 0:
                ans += 1
            return ret % k

        dfs(0, -1)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxKDivisibleComponents(5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6))
    # 3
    print(Solution().maxKDivisibleComponents(7, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[3, 0, 6, 1, 5, 2, 1], k=3))
