"""
 * 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，
 * 其中 location = [pos_x, pos_y] 且 points[i] = [x_i, y_i] 都表示 X-Y 平面上的整数坐标。
 * 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，pos_x 和 pos_y 不能改变。
 * 你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。
 * 设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。
 * 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。
 * 同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。
 * 返回你能看到的点的最大数目。
 * 提示：
 * 1、1 <= points.length <= 10^5
 * 2、points[i].length == 2
 * 3、location.length == 2
 * 4、0 <= angle < 360
 * 5、0 <= pos_x, pos_y, x_i, y_i <= 100
 * 链接：https://leetcode.cn/problems/maximum-number-of-visible-points/
"""

import bisect
import math
from typing import List

#
# @lc app=leetcode.cn id=1610 lang=python3
#
# [1610] 可见点的最大数目
#


# @lc code=start
class Solution:

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        ans, ext = 0, 0
        arr = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                ext += 1
            else:
                d = math.degrees(math.atan2(y - location[1], x - location[0]))
                if d < 0:
                    d += 360
                arr.append(d)
                arr.append(d + 360)
        arr.sort()
        for i, d in enumerate(arr):
            idx = bisect.bisect_right(arr, d + angle)
            ans = max(ans, idx - i)
        return ans + ext


# @lc code=end

if __name__ == '__main__':
    # 11
    print(Solution().visiblePoints([[60, 61], [58, 47], [17, 26], [87, 97], [63, 63], [26, 50], [70, 21], [3, 89],
                                    [51, 24], [55, 14], [6, 51], [64, 21], [66, 33], [54, 35], [87, 38], [30, 0],
                                    [37, 92], [92, 12], [60, 73], [75, 98], [1, 11], [88, 24], [82, 92]], 44, [15, 50]))
    # 2
    print(Solution().visiblePoints([[0, 0], [0, 2]], 90, [1, 1]))
    # 4
    print(Solution().visiblePoints([[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]], 0, [1, 1]))
    # 3
    print(Solution().visiblePoints([[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))
    # 4
    print(Solution().visiblePoints([[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1]))
    # 1
    print(Solution().visiblePoints([[1, 0], [2, 1]], angle=13, location=[1, 1]))
