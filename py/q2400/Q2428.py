"""
 * 给你一个大小为 m x n 的整数矩阵 grid 。
 * 按以下形式将矩阵的一部分定义为一个 沙漏 ：
 * 返回沙漏中元素的 最大 总和。
 * 注意：沙漏无法旋转且必须整个包含在矩阵中。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、3 <= m, n <= 150
 * 4、0 <= grid[i][j] <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-sum-of-an-hourglass/
"""
from typing import *


class Solution:

    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                v = grid[i][j] + grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                ans = max(ans, v)
        return ans


if __name__ == '__main__':
    # 30
    print(Solution().maxSum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]))
    # 35
    print(Solution().maxSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
