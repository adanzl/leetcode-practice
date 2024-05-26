"""
 * 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。
 * 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。
 * 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 1000
 * 4、0 <= matrix[i][j] <= 10^6
 * 5、1 <= k <= m * n
 * 链接：https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        h = []
        m, n = len(matrix), len(matrix[0])
        col = [0] * n
        for i in range(m):
            val = 0
            for j in range(n):
                col[j] ^= matrix[i][j]
                val ^= col[j]
                heappush(h, val)
                if len(h) > k:
                    heappop(h)
        return h[0]


if __name__ == '__main__':
    # 7
    print(Solution().kthLargestValue([[5, 2], [1, 6]], k=1))
    # 5
    print(Solution().kthLargestValue([[5, 2], [1, 6]], k=2))
    # 4
    print(Solution().kthLargestValue([[5, 2], [1, 6]], k=3))
    # 0
    print(Solution().kthLargestValue([[5, 2], [1, 6]], k=4))
