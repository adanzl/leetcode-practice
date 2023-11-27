"""
 * 给你一个下标从 0 开始且大小为 m x n 的整数矩阵 mat 和一个整数 k 。请你将矩阵中的 奇数 行循环 右 移 k 次，偶数 行循环 左 移 k 次。
 * 如果初始矩阵和最终矩阵完全相同，则返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= mat.length <= 25
 * 2、1 <= mat[i].length <= 25
 * 3、1 <= mat[i][j] <= 25
 * 4、1 <= k <= 50
 * 链接：https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts/
"""
from typing import List


class Solution:

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        n_mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i & 1:
                    n_mat[i][(j-k) % n] = mat[i][j]
                else:
                    n_mat[i][(j+k) % n] = mat[i][j]
        for i in range(m):
            for j in range(n):
                if mat[i][j] != n_mat[i][j]:
                    return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().areSimilar([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
    # True
    print(Solution().areSimilar([[2, 2], [2, 2]], k=3))
    # False
    print(Solution().areSimilar([[1, 2]], k=1))
