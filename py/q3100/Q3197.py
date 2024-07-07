"""
 * 给你一个二维 二进制 数组 grid。
 * 你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1 都在这些矩形的内部。
 * 返回这些矩形面积之和的 最小 可能值。
 * 注意，这些矩形可以相接。
 * 提示：
 * 1、1 <= grid.length, grid[i].length <= 30
 * 2、grid[i][j] 是 0 或 1。
 * 3、输入保证 grid 中至少有三个 1 。
 * 链接：https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii/
"""
from functools import cache
from typing import List


class Solution:

    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        LIMIT = 0x3c3c3c3c3c3c

        @cache
        def get_area(mn_i, mx_i, mn_j, mx_j):
            l, u, d, r = n, m, -1, -1,
            for i in range(mn_i, mx_i + 1):
                for j in range(mn_j, mx_j + 1):
                    if grid[i][j] == 1:
                        l, r, u, d = min(l, j), max(r, j), min(u, i), max(d, i)
            return (r - l + 1) * (d - u + 1)

        @cache
        def f(mn_i, mx_i, mn_j, mx_j, ii):
            ret = LIMIT
            # cut i
            for i in range(mn_i, mx_i):
                if ii == 1:
                    ret = min(ret, get_area(mn_i, i, mn_j, mx_j) + get_area(i + 1, mx_i, mn_j, mx_j))
                else:
                    ret = min(
                        ret,
                        get_area(mn_i, i, mn_j, mx_j) + f(i + 1, mx_i, mn_j, mx_j, 1),
                        f(mn_i, i, mn_j, mx_j, 1) + get_area(i + 1, mx_i, mn_j, mx_j),
                    )
            # cut j
            for i in range(mn_j, mx_j):
                if ii == 1:
                    ret = min(ret, get_area(mn_i, mx_i, mn_j, i) + get_area(mn_i, mx_i, i + 1, mx_j))
                else:
                    ret = min(
                        ret,
                        get_area(mn_i, mx_i, mn_j, i) + f(mn_i, mx_i, i + 1, mx_j, 1),
                        f(mn_i, mx_i, mn_j, i, 1) + get_area(mn_i, mx_i, i + 1, mx_j),
                    )
            return ret

        return f(0, m - 1, 0, n - 1, 0)


if __name__ == '__main__':
    # 5
    print(Solution().minimumSum([[1, 0, 1], [1, 1, 1]]))
    # 5
    print(Solution().minimumSum([[1, 0, 1, 0], [0, 1, 0, 1]]))
    #
    # print(Solution().minimumSum())
