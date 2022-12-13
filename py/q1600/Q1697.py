"""
 * 给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, dis_i] 表示点 ui 和点 vi 之间有一条长度为 dis_i 的边。请注意，两个点之间可能有 超过一条边 。
 * 给你一个查询数组queries ，其中 queries[j] = [pj, qj, limit_j] ，你的任务是对于每个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limit_j 。
 * 请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false 。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、1 <= edgeList.length, queries.length <= 10^5
 * 3、edgeList[i].length == 3
 * 4、queries[j].length == 3
 * 5、0 <= ui, vi, pj, qj <= n - 1
 * 6、ui != vi
 * 7、pj != qj
 * 8、1 <= dis_i, limit_j <= 10^9
 * 9、两个点之间可能有 多条 边。
 * 链接：https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/
"""
from heapq import heapify, heappop
from typing import List


class Solution:

    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:

        parent = [i for i in range(n)]
        h = []  # dis-start-end
        for s, e, v in edges:
            h.append([v, s, e])
        heapify(h)

        def find(x):
            if x != parent[x]: parent[x] = find(parent[x])
            return parent[x]

        def merge(v1, v2):
            r1, r2 = find(v1), find(v2)
            if r1 != r2: parent[r1] = r2

        ans = [False] * len(queries)
        for idx, (qs, qe, ql) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while h and h[0][0] < ql:
                _, s, e = heappop(h)
                merge(s, e)
            if find(qs) == find(qe):
                ans[idx] = True
        return ans


if __name__ == '__main__':
    # [False, True]
    print(Solution().distanceLimitedPathsExist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]))
    # [True, False]
    print(Solution().distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]))
