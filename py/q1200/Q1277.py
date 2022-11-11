"""
 * 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
 * 提示：
 * 1、1 <= arr.length <= 300
 * 2、1 <= arr[0].length <= 300
 * 3、0 <= arr[i][j] <= 1
 * 链接：https://leetcode.cn/problems/count-square-submatrices-with-all-ones/
"""
from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]  # 以f[i][j]为右下角的正方形的最大边长
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
    # 15
    print(Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
