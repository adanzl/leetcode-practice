"""
 * 给你一个二维整数数组 point ，其中 points[i] = [x_i, y_i] 表示二维平面内的一个点。
 * 同时给你一个整数 w 。你需要用矩形 覆盖所有 点。
 * 每个矩形的左下角在某个点 (x1, 0) 处，且右上角在某个点 (x2, y2) 处，其中 x1 <= x2 且 y2 >= 0 ，
 * 同时对于每个矩形都 必须 满足 x2 - x1 <= w 。
 * 如果一个点在矩形内或者在边上，我们说这个点被矩形覆盖了。
 * 请你在确保每个点都 至少 被一个矩形覆盖的前提下，最少 需要多少个矩形。
 * 注意：一个点可以被多个矩形覆盖。
 * 提示：
 * 1、1 <= points.length <= 10^5
 * 2、points[i].length == 2
 * 3、0 <= x_i == points[i][0] <= 10^9
 * 4、0 <= y_i == points[i][1] <= 10^9
 * 5、0 <= w <= 10^9
 * 6、所有点坐标 (x_i, y_i) 互不相同。
 * 链接：https://leetcode.cn/problems/minimum-rectangles-to-cover-points/
"""
from typing import List


class Solution:

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        ans = 1
        points.sort()
        pre = points[0][0]
        for i in range(1, len(points)):
            if points[i][0] - pre > w:
                ans += 1
                pre = points[i][0]
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minRectanglesToCoverPoints([[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], w=1))
    # 3
    print(Solution().minRectanglesToCoverPoints([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], w=2))
    # 2
    print(Solution().minRectanglesToCoverPoints([[2, 3], [1, 2]], w=0))
