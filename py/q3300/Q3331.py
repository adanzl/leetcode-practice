"""
 * 给你一棵 n 个节点且根节点为编号 0 的树，节点编号为 0 到 n - 1 。
 * 这棵树用一个长度为 n 的数组 parent 表示，其中 parent[i] 是第 i 个节点的父亲节点的编号。
 * 由于节点 0 是根，parent[0] == -1 。
 * 给你一个长度为 n 的字符串 s ，其中 s[i] 是节点 i 对应的字符。
 * 对于节点编号从 1 到 n - 1 的每个节点 x ，我们 同时 执行以下操作 一次 ：
 * 1、找到距离节点 x 最近 的祖先节点 y ，且 s[x] == s[y] 。
 * 2、如果节点 y 不存在，那么不做任何修改。
 * 3、否则，将节点 x 与它父亲节点之间的边 删除 ，在 x 与 y 之间连接一条边，使 y 变为 x 新的父节点。
 * 请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是 最终 树中，节点 i 为根的子树的 大小 。
 * 一个 子树 subtree 指的是节点 subtree 和它所有的后代节点。
 * 提示：
 * 1、n == parent.length == s.length
 * 2、1 <= n <= 10^5
 * 3、对于所有的 i >= 1 ，都有 0 <= parent[i] <= n - 1 。
 * 4、parent[0] == -1
 * 5、parent 表示一棵合法的树。
 * 6、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-subtree-sizes-after-changes/
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations,    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List
INF = 0x3c3c3c3c3c3c3c3c3c

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ancestor = defaultdict(lambda: -1)
        def rebuild(x: int) -> None:
            old = ancestor[s[x]]
            ancestor[s[x]] = x
            for i in range(len(g[x])):
                y = g[x][i]
                if (anc := ancestor[s[y]]) != -1:
                    g[anc].append(y)
                    g[x][i] = -1  # -1 表示删除 y
                rebuild(y)
            ancestor[s[x]] = old  # 恢复现场
        rebuild(0)

        size = [1] * n  # 注意这里已经把 1 算进去了
        def dfs(x: int) -> None:
            for y in g[x]:
                if y != -1:  # y 没被删除
                    dfs(y)
                    size[x] += size[y]
        dfs(0)
        return size

if __name__ == '__main__':
    # [19,1,15,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,2]
    print(Solution().findSubtreeSizes([-1, 10, 0, 12, 10, 18, 11, 12, 2, 3, 2, 2, 2, 0, 4, 11, 4, 2, 0],"babadabbdabcbaceeda"))
    # [6,3,1,1,1,1]
    print(Solution().findSubtreeSizes([-1, 0, 0, 1, 1, 1],"abaabc"))
    # [5,2,1,1,1]
    print(Solution().findSubtreeSizes([-1,0,4,0,1], s = "abbba"))
