"""
 * 给你一个大小为 m x n 的二元矩阵 grid ，矩阵中每个元素的值为 0 或 1 。
 * 一次 移动 是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
 * 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的 得分 就是这些数字的总和。
 * 在执行任意次 移动 后（含 0 次），返回可能的最高分数。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 20
 * 4、grid[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/score-after-flipping-matrix/
"""

from typing import List

#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#


# @lc code=start
class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = m * (1 << (n - 1))

        for j in range(1, n):
            n_ones = 0
            for i in range(m):
                if grid[i][0] == 1:
                    n_ones += grid[i][j]
                else:
                    n_ones += (1 - grid[i][j])  # 如果这一行进行了行反转，则该元素的实际取值为 1 - grid[i][j]
            k = max(n_ones, m - n_ones)
            ret += k * (1 << (n - j - 1))
        return ret


# @lc code=end

if __name__ == '__main__':
    # 39
    print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
    # 1
    print(Solution().matrixScore([[0]]))
    #
    # print(Solution().matrixScore())
