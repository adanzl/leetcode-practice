"""
 * 给你两个正整数 X 和 Y 和一个二维整数数组 circles ，
 * 其中 circles[i] = [x_i, y_i, r_i] 表示一个圆心在 (x_i, y_i) 半径为 r_i 的圆。
 * 坐标平面内有一个左下角在原点，右上角在 (X, Y) 的矩形。
 * 你需要判断是否存在一条从左下角到右上角的路径满足：
 * 路径 完全 在矩形内部，不会 触碰或者经过 任何 圆的内部和边界，同时 只 在起点和终点接触到矩形。
 * 如果存在这样的路径，请你返回 true ，否则返回 false 。
 * 提示：
 * 1、3 <= X, Y <= 10^9
 * 2、1 <= circles.length <= 1000
 * 3、circles[i].length == 3
 * 4、1 <= x_i, y_i, r_i <= 10^9
 * 链接：https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/
"""
from typing import List


class Solution:

    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        # 判断点 (x,y) 是否在圆 (ox,oy,r) 内
        def in_circle(ox: int, oy: int, r: int, x: int, y: int) -> bool:
            return (ox - x) * (ox - x) + (oy - y) * (oy - y) <= r * r

        vis = [False] * len(circles)

        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            # 圆 i 是否与矩形右边界/下边界相交相切
            if y1 <= Y and abs(x1 - X) <= r1 or \
               x1 <= X and y1 <= r1 or \
               x1 > X and in_circle(x1, y1, r1, X, 0):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                # 在两圆相交相切的前提下，点 A 是否严格在矩形内
                if not vis[j] and \
                   (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 + r2) * (r1 + r2) and \
                   x1 * r2 + x2 * r1 < (r1 + r2) * X and \
                   y1 * r2 + y2 * r1 < (r1 + r2) * Y and \
                   dfs(j):
                    return True
            return False

        for i, (x, y, r) in enumerate(circles):
            # 圆 i 包含矩形左下角 or 圆 i 包含矩形右上角
            if in_circle(x, y, r, 0, 0) or in_circle(x, y, r, X, Y):
                return False
            # 圆 i 与矩形上边界/左边界相交相切
            inter_up = x <= X and abs(y - Y) <= r
            inter_in = y <= Y and x <= r
            inter_right = y > Y and in_circle(x, y, r, 0, Y)
            if not vis[i] and (inter_up or inter_in or inter_right) and dfs(i):
                return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().canReachCorner(15, 15, [[1, 99, 85], [99, 1, 85]]))
    # True
    print(Solution().canReachCorner(4, 4, [[5, 5, 1]]))
    # True
    print(Solution().canReachCorner(3, Y=4, circles=[[2, 1, 1]]))
    # False
    print(Solution().canReachCorner(3, Y=3, circles=[[1, 1, 2]]))
    # False
    print(Solution().canReachCorner(3, Y=3, circles=[[2, 1, 1], [1, 2, 1]]))
