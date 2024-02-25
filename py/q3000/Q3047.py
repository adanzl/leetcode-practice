"""
 * 在二维平面上存在 n 个矩形。给你两个下标从 0 开始的二维整数数组 bottomLeft 和 topRight，两个数组的大小都是 n x 2 ，
 * 其中 bottomLeft[i] 和 topRight[i] 分别代表第 i 个矩形的 左下角 和 右上角 坐标。
 * 我们定义 向右 的方向为 x 轴正半轴（x 坐标增加），向左 的方向为 x 轴负半轴（x 坐标减少）。
 * 同样地，定义 向上 的方向为 y 轴正半轴（y 坐标增加），向下 的方向为 y 轴负半轴（y 坐标减少）。
 * 你可以选择一个区域，该区域由两个矩形的 交集 形成。你需要找出能够放入该区域 内 的 最大 正方形面积，并选择最优解。
 * 返回能够放入交集区域的正方形的 最大 可能面积，如果矩形之间不存在任何交集区域，则返回 0
 * 提示：
 * 1、n == bottomLeft.length == topRight.length
 * 2、2 <= n <= 10^3
 * 3、bottomLeft[i].length == topRight[i].length == 2
 * 4、1 <= bottomLeft[i][0], bottomLeft[i][1] <= 10^7
 * 5、1 <= topRight[i][0], topRight[i][1] <= 10^7
 * 6、bottomLeft[i][0] < topRight[i][0]
 * 7、bottomLeft[i][1] < topRight[i][1]
 * 链接：https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles/
"""
from typing import List


class Solution:

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        arr = [[x0, y0, x1, y1] for (x0, y0), (x1, y1) in zip(bottomLeft, topRight)]
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x0, y0, x1, y1 = arr[i]
                x2, y2, x3, y3 = arr[j]
                if x1 < x2 or x3 < x0 or y1 < y2 or y3 < y0:
                    continue
                w = min(x1, x3) - max(x0, x2)
                h = min(y1, y3) - max(y0, y2)
                ans = max(ans, min(h, w))
        return ans**2


if __name__ == '__main__':
    # 4
    print(Solution().largestSquareArea([[2, 2], [3, 1]], [[5, 5], [5, 5]]))
    # 1
    print(Solution().largestSquareArea([[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [4, 4], [6, 6]]))
    # 1
    print(Solution().largestSquareArea([[1, 1], [2, 2], [1, 2]], topRight=[[3, 3], [4, 4], [3, 4]]))
    # 0
    print(Solution().largestSquareArea([[1, 1], [3, 3], [3, 1]], topRight=[[2, 2], [4, 4], [4, 2]]))
