"""
 * 给你一个下标从 0 开始、大小为 m x n 的二维矩阵 grid ，请你求解大小同样为 m x n 的答案矩阵 answer 。
 * 矩阵 answer 中每个单元格 (r, c) 的值可以按下述方式进行计算：
 * 1、令 topLeft[r][c] 为矩阵 grid 中单元格 (r, c) 左上角对角线上 不同值 的数量。
 * 2、令 bottomRight[r][c] 为矩阵 grid 中单元格 (r, c) 右下角对角线上 不同值 的数量。
 * 然后 answer[r][c] = |topLeft[r][c] - bottomRight[r][c]| 。
 * 返回矩阵 answer 。
 * 矩阵对角线 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。
 * 如果单元格 (r1, c1) 和单元格 (r, c) 属于同一条对角线且 r1 < r ，则单元格 (r1, c1) 属于单元格 (r, c) 的左上对角线。类似地，可以定义右下对角线。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n, grid[i][j] <= 50
 * 链接：https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/
"""
from typing import List


class Solution:

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l, r = set(), set()
                ii, jj = i + 1, j + 1
                while ii < m and jj < n:
                    r.add(grid[ii][jj])
                    ii += 1
                    jj += 1
                ii, jj = i - 1, j - 1
                while ii >= 0 and jj >= 0:
                    l.add(grid[ii][jj])
                    ii -= 1
                    jj -= 1
                ans[i][j] = abs(len(r) - len(l))
        return ans


if __name__ == '__main__':
    # [[1,1,0],[1,0,1],[0,1,1]]
    print(Solution().differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
    # [[0]]
    print(Solution().differenceOfDistinctValues([[1]]))