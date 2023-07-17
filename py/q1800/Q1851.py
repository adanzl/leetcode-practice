"""
 * 给你一个二维整数数组 intervals ，其中 intervals[i] = [left_i, right_i] 表示第 i 个区间开始于 left_i 、
 * 结束于 right_i（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 right_i - left_i + 1 。
 * 再给你一个整数数组 queries 。第 j 个查询的答案是满足 left_i <= queries[j] <= right_i 的 长度最小区间 i 的长度 。
 * 如果不存在这样的区间，那么答案是 -1 。
 * 以数组形式返回对应查询的所有答案。
 * 提示：
 * 1、1 <= intervals.length <= 10^5
 * 2、1 <= queries.length <= 10^5
 * 3、queries[i].length == 2
 * 4、1 <= left_i <= right_i <= 10^7
 * 5、1 <= queries[j] <= 10^7
 * 链接：https://leetcode.cn/problems/minimum-interval-to-include-each-query/
"""
from heapq import heappop, heappush
from typing import List

from sortedcontainers import SortedDict


class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        ans = {}
        intervals.sort()
        idx, h = 0, []
        for q in sorted(queries):
            while idx < n and intervals[idx][0] <= q:
                l, r = intervals[idx]
                idx += 1
                heappush(h, (r - l + 1, r))
            while h and h[0][1] < q:
                heappop(h)
            ans[q] = h[0][0] if h else -1
        return [ans[q] for q in queries]

    def minInterval1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        ans = [-1] * n
        s_d = SortedDict()
        s_l = sorted([[r - l + 1, l, r] for l, r in intervals])
        for i, q in enumerate(queries):
            if not q in s_d:
                s_d[q] = []
            s_d[q].append(i)
        for s, l, r in s_l:
            idx_l = s_d.bisect_left(l)
            idx_r = s_d.bisect_right(r)
            if idx_l == idx_r:
                continue
            for k in s_d.keys()[idx_l:idx_r]:
                v = s_d[k]
                for i in v:
                    ans[i] = s
                del s_d[k]
        return ans


if __name__ == '__main__':
    # [3,3,1,4]
    print(Solution().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5]))
    # [2,-1,4,6]
    print(Solution().minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22]))
