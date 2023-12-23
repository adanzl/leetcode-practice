"""
 * 平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi] 。请你计算访问所有这些点需要的 最小时间（以秒为单位）。
 * 你需要按照下面的规则在平面上移动：
 * 1、每一秒内，你可以：
 *  沿水平方向移动一个单位长度，或者
 *  沿竖直方向移动一个单位长度，或者
 *  跨过对角线移动 sqrt(2) 个单位长度（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
 * 2、必须按照数组中出现的顺序来访问这些点。
 * 3、在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。
 * 提示：
 * 1、points.length == n
 * 2、1 <= n <= 100
 * 3、points[i].length == 2
 * 4、-1000 <= points[i][0], points[i][1] <= 1000
 * 链接：https://leetcode.cn/problems/minimum-time-visiting-all-points
"""
from typing import List


class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x0, x1 = points[0]
        ans = 0
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
    # 5
    print(Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
