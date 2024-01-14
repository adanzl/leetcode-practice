"""
 * 给你一个下标从 0 开始的二维整数数组 dimensions。
 * 对于所有下标 i（0 <= i < dimensions.length），dimensions[i][0] 表示矩形 i 的长度，而 dimensions[i][1] 表示矩形 i 的宽度。
 * 返回对角线最 长 的矩形的 面积 。如果存在多个对角线长度相同的矩形，返回面积最 大 的矩形的面积。
 * 提示：
 * 1、1 <= dimensions.length <= 100
 * 2、dimensions[i].length == 2
 * 3、1 <= dimensions[i][0], dimensions[i][1] <= 100
 * 链接：https://leetcode.cn/problems/maximum-area-of-longest-diagonal-rectangle/
"""
from typing import List


class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        ln = 0
        for a, b in dimensions:
            nv = a * a + b * b
            if nv > ln:
                ln = nv
                ans = a * b
            elif nv == ln:
                ans = max(ans, a * b)
        return ans


if __name__ == '__main__':
    # 20
    print(Solution().areaOfMaxDiagonal([[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]))
    # 48
    print(Solution().areaOfMaxDiagonal([[9, 3], [8, 6]]))
    # 12
    print(Solution().areaOfMaxDiagonal([[3, 4], [4, 3]]))
