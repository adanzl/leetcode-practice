"""
 * 给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。
 * 两点之间的距离定义为它们的 曼哈顿距离 。
 * 请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。
 * 提示：
 * 1、3 <= points.length <= 10^5
 * 2、points[i].length == 2
 * 3、1 <= points[i][0], points[i][1] <= 10^8
 * 链接：https://leetcode.cn/problems/minimize-manhattan-distances/description/
"""
from typing import List

from sortedcontainers import SortedList


class Solution:

    def minimumDistance(self, points: List[List[int]]) -> int:
        # 曼哈顿距离与切比雪夫距离的相互转化 https://oi-wiki.org/geometry/distance/#%E5%AE%9A%E4%B9%89_3
        # 切比雪夫距离定义：二个点之间各坐标数值差的最大值
        # 将一个点 (x,y) 的坐标变为 (x + y, x - y) 后，原坐标系中的曼哈顿距离等于新坐标系中的切比雪夫距离
        # 求任意两点曼哈顿距离的最大值，等价计算任意两个点 切比雪夫距离 的最大值，即横纵坐标差的最大值
        xs = SortedList()
        ys = SortedList()
        for x, y in points:
            xs.add(x + y)
            ys.add(y - x)
        ans = 0x3c3c3c3c3c3c
        for x, y in points:
            x, y = x + y, y - x
            xs.remove(x)
            ys.remove(y)
            ans = min(ans, max(xs[-1] - xs[0], ys[-1] - ys[0]))  # type:ignore
            xs.add(x)
            ys.add(y)
        return ans


if __name__ == '__main__':
    # 12
    print(Solution().minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))
    # 0
    print(Solution().minimumDistance([[1, 1], [1, 1], [1, 1]]))
    #
    # print(Solution().minimumDistance())
