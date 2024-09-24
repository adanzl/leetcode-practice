"""
 * 给你一个由正整数构成的二维矩阵 grid。
 * 你需要从矩阵中选择 一个或多个 单元格，选中的单元格应满足以下条件：
 * 1、所选单元格中的任意两个单元格都不会处于矩阵的 同一行。
 * 2、所选单元格的值 互不相同。
 * 你的得分为所选单元格值的总和。
 * 返回你能获得的 最大 得分。
 * 提示：
 * 1、1 <= grid.length, grid[i].length <= 10
 * 2、1 <= grid[i][j] <= 100
 * 链接：https://leetcode.cn/problems/select-cells-in-grid-with-maximum-score/
"""
from functools import cache
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxScore(self, grid: List[List[int]]) -> int:
        mx = max(map(max, grid))
        pos = [[] for _ in range(mx + 1)]
        for i, row in enumerate(grid):
            for x in set(row):  # 去重
                pos[x].append(i)

        @cache
        def dfs(val, s_r):
            if val == 0:
                return 0
            ret = dfs(val - 1, s_r)
            for l in pos[val]:
                if 1 << l & s_r: continue
                ret = max(ret, val + dfs(val - 1, s_r | 1 << l))
            return ret

        return dfs(mx, 0)


if __name__ == '__main__':
    # 8
    print(Solution().maxScore([[1, 2, 3], [4, 3, 2], [1, 1, 1]]))
    # 15
    print(Solution().maxScore([[8, 7, 6], [8, 3, 2]]))
    # 797
    print(Solution().maxScore([
        [92, 11, 45, 88, 38, 13, 65, 85],
        [52, 83, 3, 14, 82, 51, 27, 59],
        [65, 69, 99, 27, 7, 70, 39, 43],
        [43, 46, 22, 19, 75, 70, 57, 50],
        [54, 36, 91, 80, 74, 43, 62, 61],
        [35, 45, 19, 32, 92, 50, 93, 88],
        [60, 15, 93, 10, 89, 32, 51, 11],
        [82, 66, 42, 61, 78, 94, 66, 7],
        [75, 56, 49, 78, 81, 61, 79, 50],
    ]))
