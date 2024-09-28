"""
 * 有一个无限大的二维平面。
 * 给你一个正整数 k ，同时给你一个二维数组 queries ，包含一系列查询：
 * queries[i] = [x, y] ：在平面上坐标 (x, y) 处建一个障碍物，数据保证之前的查询 不会 在这个坐标处建立任何障碍物。
 * 每次查询后，你需要找到离原点第 k 近 障碍物到原点的 距离 。
 * 请你返回一个整数数组 results ，其中 results[i] 表示建立第 i 个障碍物以后，离原地第 k 近障碍物距离原点的距离。
 * 如果少于 k 个障碍物，results[i] == -1 。
 * 注意，一开始 没有 任何障碍物。
 * 坐标在 (x, y) 处的点距离原点的距离定义为 |x| + |y| 。
 * 提示：
 * 1、1 <= queries.length <= 2 * 10^5
 * 2、所有 queries[i] 互不相同。
 * 3、-10^9 <= queries[i][0], queries[i][1] <= 10^9
 * 4、1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/k-th-nearest-obstacle-queries/
"""
from heapq import heappush, heappushpop
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = []
        h = []
        for x, y in queries:
            if len(h) >= k:
                heappushpop(h, -abs(x) - abs(y))
            else:
                heappush(h, -abs(x) - abs(y))
            if len(h) == k:
                ans.append(-h[0])
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    # [10,10,3,3,3]
    print(Solution().resultsArray([[-6, 4], [7, 8], [-2, -1], [1, -9], [-9, 4]], 1))
    # [9]
    print(Solution().resultsArray([[-6, 3]], 1))
    # [-1,7,5,3]
    print(Solution().resultsArray([[1, 2], [3, 4], [2, 3], [-3, 0]], k=2))
    # [10,8,6]
    print(Solution().resultsArray([[5, 5], [4, 4], [3, 3]], k=1))
