"""
 * 给你一个下标从 0 开始、大小为 n x n 的矩阵 grid ，其中 n 为奇数，且 grid[r][c] 的值为 0 、1 或 2 。
 * 如果一个单元格属于以下三条线中的任一一条，我们就认为它是字母 Y 的一部分：
 * 1、从左上角单元格开始到矩阵中心单元格结束的对角线。
 * 2、从右上角单元格开始到矩阵中心单元格结束的对角线。
 * 3、从中心单元格开始到矩阵底部边界结束的垂直线。
 * 当且仅当满足以下全部条件时，可以判定矩阵上写有字母 Y ：
 * 1、属于 Y 的所有单元格的值相等。
 * 2、不属于 Y 的所有单元格的值相等。
 * 3、属于 Y 的单元格的值与不属于Y的单元格的值不同。
 * 每次操作你可以将任意单元格的值改变为 0 、1 或 2 。返回在矩阵上写出字母 Y 所需的 最少 操作次数。
 * 提示：
 * 1、3 <= n <= 49
 * 2、n == grid.length == grid[i].length
 * 3、0 <= grid[i][j] <= 2
 * 4、n 为奇数。
 * 链接：https://leetcode.cn/problems/minimum-operations-to-write-the-letter-y-on-a-grid/description/
"""
from typing import List


class Solution:

    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        ans = 10**9
        n = len(grid)
        for y, ny in [[0, 2], [0, 1], [1, 0], [1, 2], [2, 1], [2, 0]]:
            vv = 0
            for i in range(n):
                for j in range(n):
                    if i < n // 2:
                        if j < n // 2:
                            if i == j:  # condition 1
                                if grid[i][j] != y:
                                    vv += 1
                            else:
                                if grid[i][j] != ny:
                                    vv += 1
                        else:
                            if i == n - 1 - j:  # condition 2
                                if grid[i][j] != y:
                                    vv += 1
                            else:
                                if grid[i][j] != ny:
                                    vv += 1
                    else:
                        if j == n // 2:  # condition 3
                            if grid[i][j] != y:
                                vv += 1
                        else:
                            if grid[i][j] != ny:
                                vv += 1
            ans = min(ans, vv)
        return ans


if __name__ == '__main__':
    # 12
    print(Solution().minimumOperationsToWriteY([[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2],
                                                [2, 1, 2, 2, 2]]))
    # 3
    print(Solution().minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
    #
    # print(Solution().minimumOperationsToWriteY())
