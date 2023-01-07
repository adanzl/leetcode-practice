"""
 * 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [x_start, x_end] 表示水平直径在 x_start 和 x_end之间的气球。
 * 你不知道气球的确切 y 坐标。
 * 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。
 * 在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 x_start，x_end， 且满足  x_start ≤ x ≤ x_end，则该气球会被 引爆 。
 * 可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
 * 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
 * 提示:
 * 1、1 <= points.length <= 10^5
 * 2、points[i].length == 2
 * 3、-2^31 <= x_start < x_end <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        p = points[0][1]
        ans = 1
        for b in points:
            if b[0] > p:
                p = b[1]
                ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    # 4
    print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    # 2
    print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
