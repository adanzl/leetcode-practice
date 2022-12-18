"""
 * 给你一个整数 n ，表示你有一棵含有 2n - 1 个节点的 完全二叉树 。根节点的编号是 1 ，树中编号在[1, 2n - 1 - 1] 之间，编号为 val 的节点都有两个子节点，满足：
 * 1、左子节点的编号为 2 * val
 * 2、右子节点的编号为 2 * val + 1
 * 给你一个长度为 m 的查询数组 queries ，它是一个二维整数数组，其中 queries[i] = [ai, bi] 。对于每个查询，求出以下问题的解：
 * 1、在节点编号为 ai 和 bi 之间添加一条边。
 * 2、求出图中环的长度。
 * 3、删除节点编号为 ai 和 bi 之间新添加的边。
 * 注意：
 * 1、环 是开始和结束于同一节点的一条路径，路径中每条边都只会被访问一次。
 * 2、环的长度是环中边的数目。
 * 3、在树中添加额外的边后，两个点之间可能会有多条边。
 * 请你返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 个查询的结果。
 * 提示：
 * 1、2 <= n <= 30
 * 2、m == queries.length
 * 3、1 <= m <= 10^5
 * 4、queries[i].length == 2
 * 5、1 <= ai, bi <= 2n - 1
 * 6、ai != bi
 * 链接：https://leetcode.cn/problems/cycle-length-queries-in-a-tree/
"""
from typing import List


class Solution:

    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        deep = lambda x: x.bit_length()

        def lca(p, q):  # 完全二叉树的最近公共祖先
            while q != p:
                if p > q: p >>= 1
                else: q >>= 1
            return p

        ans = [0] * len(queries)
        for i, (p, q) in enumerate(queries):
            if p == q: continue
            ans[i] = deep(p) + deep(q) - 2 * deep(lca(p, q)) + 1
        return ans


if __name__ == '__main__':
    # [4,5,3]
    print(Solution().cycleLengthQueries(3, queries=[[5, 3], [4, 7], [2, 3]]))
    # [2]
    print(Solution().cycleLengthQueries(2, queries=[[1, 2]]))
