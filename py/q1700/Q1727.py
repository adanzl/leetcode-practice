"""
 * 给你一个二进制矩阵 matrix ，它的大小为 m x n ，你可以将 matrix 中的 列 按任意顺序重新排列。
 * 请你返回最优方案下将 matrix 重新排列后，全是 1 的子矩阵面积。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m * n <= 10^5
 * 4、matrix[i][j] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.cn/problems/largest-submatrix-with-rearrangements
"""

from typing import List

#
# @lc app=leetcode.cn id=1727 lang=python3
#
# [1727] 重新排列后的最大子矩阵
#


# @lc code=start
class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        arr = [[0] * (m) for _ in range(n)]
        for j in range(n):
            for i in range(m - 1, -1, -1):
                if matrix[i][j]:
                    pre = arr[j][i + 1] if i < m - 1 else 0
                    arr[j][i] = pre + 1
                else:
                    arr[j][i] = 0
        ans = 0
        for i in range(m):
            a = sorted(arr, key=lambda x: x[i], reverse=True)
            h = m
            for j in range(n):
                h = min(h, a[j][i])
                ans = max(ans, h * (j + 1))
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
    # 3
    print(Solution().largestSubmatrix([[1, 0, 1, 0, 1]]))
    # 2
    print(Solution().largestSubmatrix([[1, 1, 0], [1, 0, 1]]))
    # 0
    print(Solution().largestSubmatrix([[0, 0], [0, 0]]))
