"""
 * 给你一个整数 n 和一个二维整数数组 queries。
 * 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
 * queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
 * 所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
 * 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，
 * answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。
 * 提示:
 * 1、3 <= n <= 10^5
 * 2、1 <= queries.length <= 10^5
 * 3、queries[i].length == 2
 * 4、0 <= queries[i][0] < queries[i][1] < n
 * 5、1 < queries[i][1] - queries[i][0]
 * 6、查询中不存在重复的道路。
 * 7、不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
 * 链接：https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/
"""
import bisect
from typing import List


class Solution:

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append([i + 1, 1])
        arr = [i for i in range(n)]
        ans = []
        for u, v in queries:
            iu = bisect.bisect_right(arr, u)
            iv = bisect.bisect_left(arr, v)
            del arr[iu:iv]
            ans.append(len(arr) - 1)
        return ans


if __name__ == '__main__':
    # [2,2]
    print(Solution().shortestDistanceAfterQueries(5, [[1, 4], [2, 4]]))
    # [3, 2, 1]
    print(Solution().shortestDistanceAfterQueries(5, queries=[[2, 4], [0, 2], [0, 4]]))
    # [1, 1]
    print(Solution().shortestDistanceAfterQueries(4, queries=[[0, 3], [0, 2]]))
