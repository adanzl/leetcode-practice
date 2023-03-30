"""
 * 给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。
 * 垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。
 * 请注意，垂直区域 边上 的点 不在 区域内。
 * 提示：
 * 1、n == points.length
 * 2、2 <= n <= 10^5
 * 3、points[i].length == 2
 * 4、0 <= xi, yi <= 10^9
 * 链接：https://leetcode.cn/problems/widest-vertical-area-between-two-points-containing-no-points/
"""
from itertools import pairwise
from typing import List


class Solution:

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(p1 - p0 for p0, p1 in pairwise(sorted(p[0] for p in points)))


if __name__ == '__main__':
    # 1
    print(Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
    # 3
    print(Solution().maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
    #
    # print(Solution().maxWidthOfVerticalArea())