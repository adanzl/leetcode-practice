"""
 * 给你一个下标从 0 开始的 m x n 二进制矩阵 grid 。
 * 我们按照如下过程，定义一个下标从 0 开始的 m x n 差值矩阵 diff ：
 * 1、令第 i 行一的数目为 onesRow_i 。
 * 2、令第 j 列一的数目为 onesCol_j 。
 * 3、令第 i 行零的数目为 zerosRow_i 。
 * 4、令第 j 列零的数目为 zerosCol_j 。
 * 5、diff[i][j] = onesRow_i + onesCol_j - zerosRow_i - zerosCol_j
 * 请你返回差值矩阵 diff 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 10^5
 * 5、grid[i][j] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.cn/problems/difference-between-ones-and-zeros-in-row-and-column/
"""
from typing import List


class Solution:

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        ans = [[0] * col for _ in range(row)]
        one_col, zero_col = [0] * col, [0] * col
        one_row, zero_row = [0] * row, [0] * row

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    one_row[i] += 1
                    one_col[j] += 1
                else:
                    zero_row[i] += 1
                    zero_col[j] += 1
        for i in range(row):
            for j in range(col):
                ans[i][j] = one_row[i] + one_col[j] - zero_row[i] - zero_col[j]
        return ans


if __name__ == '__main__':
    # [[0,0,4],[0,0,4],[-2,-2,2]]
    print(Solution().onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
    # [[5,5,5],[5,5,5]]
    print(Solution().onesMinusZeros([[1, 1, 1], [1, 1, 1]]))
