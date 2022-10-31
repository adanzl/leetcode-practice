"""
 * 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
 * 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 20
 * 4、0 <= matrix[i][j] <= 99
 * 进阶：
 * 1、如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
 * 2、如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
 * 链接：https://leetcode-cn.com/problems/toeplitz-matrix
"""
from typing import List


class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if i > j:
                    if matrix[i - j][0] != matrix[i][j]: return False
                else:
                    if matrix[0][j - i] != matrix[i][j]: return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
    # False
    print(Solution().isToeplitzMatrix([[1, 2], [2, 2]]))
