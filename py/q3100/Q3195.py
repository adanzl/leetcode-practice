"""
 * 给你一个二维 二进制 数组 grid。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 grid 中所有的 1 都在矩形的内部。
 * 返回这个矩形可能的 最小 面积。
 * 提示：
 * 1、1 <= grid.length, grid[i].length <= 1000
 * 2、grid[i][j] 是 0 或 1。
 * 3、输入保证 grid 中至少有一个 1 。
 * 链接：https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/
"""
from typing import List


class Solution:

    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l, u, d, r = n, m, -1, -1,
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    l = min(l, j)
                    r = max(r, j)
                    u = min(u, i)
                    d = max(d, i)
        return (r - l + 1) * (d - u + 1)


if __name__ == '__main__':
    # 1
    print(Solution().minimumArea([[0, 0], [1, 0]]))
    # 6
    print(Solution().minimumArea([[0, 1, 0], [1, 0, 1]]))
    #
    # print(Solution().minimumArea())
