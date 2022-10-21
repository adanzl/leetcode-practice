"""
 * 你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
 * 假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。
 * 返回 多边形进行三角剖分后可以得到的最低分 。
 * 提示：
 * 1、n == values.length
 * 2、3 <= n <= 50
 * 3、1 <= values[i] <= 100
 * 链接：https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/
"""
from functools import cache
from typing import List


class Solution:

    def minScoreTriangulation(self, values: List[int]) -> int:
        inf = 0x3c3c3c3c

        @cache
        def dfs(left, right):
            if right - left + 1 < 3: return 0
            res = inf
            for i in range(left + 1, right):
                res = min(res, values[left] * values[right] * values[i] + dfs(left, i) + dfs(i, right))
            return res

        return dfs(0, len(values) - 1)


if __name__ == '__main__':
    # 6
    print(Solution().minScoreTriangulation([1, 2, 3]))
    # 144
    print(Solution().minScoreTriangulation([3, 7, 4, 5]))
    # 13
    print(Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5]))
