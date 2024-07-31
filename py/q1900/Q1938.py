"""
 * 给你一棵 n 个节点的有根树，节点编号从 0 到 n - 1 。
 * 每个节点的编号表示这个节点的 独一无二的基因值 （也就是说节点 x 的基因值为 x）。
 * 两个基因值的 基因差 是两者的 异或和 。给你整数数组 parents ，其中 parents[i] 是节点 i 的父节点。
 * 如果节点 x 是树的 根 ，那么 parents[x] == -1 。
 * 给你查询数组 queries ，其中 queries[i] = [node_i, val_i] 。
 * 对于查询 i ，请你找到 val_i 和 pi 的 最大基因差 ，其中 p_i 是节点 node_i 到根之间的任意节点（包含 node_i 和根节点）。
 * 更正式的，你想要最大化 val_i XOR p_i 。
 * 请你返回数组 ans ，其中 ans[i] 是第 i 个查询的答案。
 * 提示：
 * 1、2 <= parents.length <= 10^5
 * 2、对于每个 不是 根节点的 i ，有 0 <= parents[i] <= parents.length - 1 。
 * 3、parents[root] == -1
 * 4、1 <= queries.length <= 3 * 10^4
 * 5、0 <= node_i <= parents.length - 1
 * 6、0 <= val_i <= 2 * 10^5
 * 链接：https://leetcode.cn/problems/maximum-genetic-difference-query/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=1938 lang=python3
#
# [1938] 查询最大基因差
#


# @lc code=start
class Solution:

    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        N = 20
        n, r = len(parents), -1
        g = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1: r = i
            else: g[p].append(i)

        tree = [0] * (1 << N + 1)

        def update(node, num, f):
            cur = node
            for i in range(N):
                if not num & (1 << (N - i - 1)):
                    nxt = cur * 2 + 1
                else:
                    nxt = cur * 2 + 2
                tree[nxt] += f
                cur = nxt

        def query(node, num):
            cur = node
            ret = num
            for i in range(N):
                sign = 1 << (N - i - 1)
                if not num & sign:  # num i 位为 0
                    if tree[cur * 2 + 2]:  # 子树有 1
                        cur = cur * 2 + 2
                        ret += sign
                    else:
                        cur = cur * 2 + 1
                else:  # num i 位为 1
                    if tree[cur * 2 + 1]:  #  子树有 0
                        cur = cur * 2 + 1
                    else:
                        cur = cur * 2 + 2
                        ret -= sign
            return ret

        def dfs(idx):
            update(0, idx, 1)
            for ii in q_map[idx]:
                ans[ii] = query(0, queries[ii][1])
            for nx in g[idx]:
                dfs(nx)
            update(0, idx, -1)

        ans = [0] * len(queries)
        q_map = defaultdict(list)
        for i, (o, val) in enumerate(queries):
            q_map[o].append(i)

        dfs(r)
        return ans


# @lc code=end

if __name__ == '__main__':
    # [6,14,7]
    print(Solution().maxGeneticDifference([3, 7, -1, 2, 0, 7, 0, 2], queries=[[4, 6], [1, 15], [0, 5]]))
    # [2,3,7]
    print(Solution().maxGeneticDifference([-1, 0, 1, 1], queries=[[0, 2], [3, 2], [2, 5]]))
    #
    # print(Solution().maxGeneticDifference())
