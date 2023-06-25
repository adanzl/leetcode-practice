"""
 * 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，
 * 其中 (x1, y1) 是矩形左下角的坐标，而 (x2, y2) 是右上角的坐标。
 * 如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。
 * 换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。
 * 提示：
 * 1、1 <= radius <= 2000
 * 2、-10^4 <= xCenter, yCenter <= 10^4
 * 3、-10^4 <= x1 < x2 <= 10^4
 * 4、-10^4 <= y1 < y2 <= 10^4
 * 链接：https://leetcode.cn/problems/circle-and-rectangle-overlapping/
"""


class Solution:

    def checkOverlap(self, radius: int, x: int, y: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dis = lambda x0, y0, x1, y1: ((x0 - x1)**2 + (y0 - y1)**2)
        d1, d2, d3, d4 = dis(x, y, x1, y1), dis(x, y, x1, y2), dis(x, y, x2, y1), dis(x, y, x2, y2)
        mx, mn = max(d1, d2, d3, d4), min(d1, d2, d3, d4)
        if y1 <= y <= y2:
            mn = min(abs(x - x1), abs(x - x2), mn)**2
        if x1 <= x <= x2:
            mn = min(abs(y - y1), abs(y - y2), mn)**2
        return mn <= radius**2 or (x1 <= x <= x2 and y1 <= y <= y2)


if __name__ == '__main__':
    # True
    print(Solution().checkOverlap(24, x=13, y=1, x1=0, y1=15, x2=5, y2=18))
    # True
    print(Solution().checkOverlap(1, x=1, y=1, x1=-3, y1=-3, x2=3, y2=3))
    # True
    print(Solution().checkOverlap(1, x=0, y=0, x1=1, y1=-1, x2=3, y2=1))
    # False
    print(Solution().checkOverlap(1, x=1, y=1, x1=1, y1=-3, x2=2, y2=-1))
    # True
    print(Solution().checkOverlap(1, x=0, y=0, x1=-1, y1=0, x2=0, y2=1))
