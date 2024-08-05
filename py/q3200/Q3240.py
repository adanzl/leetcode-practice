"""
 * 给你一个 m x n 的二进制矩阵 grid 。
 * 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
 * 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
 * 请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 1 的数目可以被 4 整除 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m * n <= 2 * 10^5
 * 4、0 <= grid[i][j] <= 1
 * 链接：https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/
"""
from itertools import product
from typing import List


class Solution:

    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans, ans_2 = 0, 0
        cross_1 = 0  # 中心线上成对的 1

        for i, j in product(range(m // 2), range(n // 2)):
            s = grid[i][j] + grid[m - 1 - i][j] + grid[i][n - 1 - j] + grid[m - 1 - i][n - 1 - j]
            ans += min(s, 4 - s)

        if m & 1:
            for j in range(n // 2):
                if grid[m // 2][j] != grid[m // 2][n - 1 - j]:
                    ans += 1
                    ans_2 += 1  # 1 变成 0
                    cross_1 += 2
                elif grid[m // 2][j]:
                    cross_1 += 2
        if n & 1:
            for i in range(m // 2):
                if grid[i][n // 2] != grid[m - 1 - i][n // 2]:
                    ans += 1
                    ans_2 += 1  #  1 变成 0
                    cross_1 += 2
                elif grid[i][n // 2]:
                    cross_1 += 2
        if m & 1 and n & 1:
            ans += grid[m // 2][n // 2]
        r1 = cross_1 % 4
        if r1 == 2:
            return ans if ans_2 else (ans + 2)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minFlips([[0, 1], [0, 1], [0, 0]]))
    # 3
    print(Solution().minFlips([[1, 0, 0], [0, 0, 1], [0, 0, 1]]))
    # 3
    print(Solution().minFlips([[1, 1, 1], [1, 1, 0]]))
    # 2
    print(Solution().minFlips([[1], [1]]))
    # 3
    print(Solution().minFlips([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
