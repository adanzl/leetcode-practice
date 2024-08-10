"""
 * 给你一个 m x n 的二进制矩阵 grid 。
 * 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
 * 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
 * 请你返回 最少 翻转次数，使得矩阵 要么 所有行是 回文的 ，要么所有列是 回文的 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m * n <= 2 * 10^5
 * 4、0 <= grid[i][j] <= 1
 * 链接：https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
"""
from typing import List


class Solution:

    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans_c, ans_r = 0, 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - 1 - j]:
                    ans_r += 1
        for i in range(m // 2):
            for j in range(n):
                if grid[i][j] != grid[m - i - 1][j]:
                    ans_c += 1
        return min(ans_c, ans_r)


if __name__ == '__main__':
    # 2
    print(Solution().minFlips([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
    # 1
    print(Solution().minFlips([[0, 1], [0, 1], [0, 0]]))
    # 0
    print(Solution().minFlips([[1], [0]]))
