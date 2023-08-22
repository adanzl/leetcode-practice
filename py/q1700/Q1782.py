"""
 * 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
 * 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
 * 1、a < b
 * 2、cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
 * 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
 * 请注意，图中可能会有 重复边 。
 * 提示：
 * 1、2 <= n <= 2 * 10^4
 * 2、1 <= edges.length <= 10^5
 * 3、1 <= ui, vi <= n
 * 4、ui != vi
 * 5、1 <= queries.length <= 20
 * 6、0 <= queries[j] < edges.length
 * 链接：https://leetcode.cn/problems/count-pairs-of-nodes/
"""
import bisect
from typing import Counter, List


class Solution:

    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        e = Counter()
        c = [0] * (n)
        for edge in edges:
            a, b = edge[0] - 1, edge[1] - 1
            if a > b:
                a, b = b, a
            e[(a, b)] += 1
            c[a] += 1
            c[b] += 1
        arr = sorted(c)
        ans = []
        for q in queries:
            tot = 0
            for i in range(n):
                idx = bisect.bisect_right(arr, q - arr[i], i + 1)
                tot += n - idx
            for v, k in e.items():
                if c[v[0]] + c[v[1]] > q >= c[v[0]] + c[v[1]] - k:
                    tot -= 1
            ans.append(tot)
        return ans


if __name__ == '__main__':
    # [6,5]
    print(Solution().countPairs(4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3]))
    # [10,10,9,8,6]
    print(Solution().countPairs(5, edges=[[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]], queries=[1, 2, 3, 4, 5]))