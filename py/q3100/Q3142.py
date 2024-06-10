"""
 * 给你一个大小为 m x n 的二维矩阵 grid 。你需要判断每一个格子 grid[i][j] 是否满足：
 * 1、如果它下面的格子存在，那么它需要等于它下面的格子，也就是 grid[i][j] == grid[i + 1][j] 。
 * 2、如果它右边的格子存在，那么它需要不等于它右边的格子，也就是 grid[i][j] != grid[i][j + 1] 。
 * 如果 所有 格子都满足以上条件，那么返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= n, m <= 10
 * 2、0 <= grid[i][j] <= 9
 * 链接：https://leetcode.cn/problems/check-if-grid-satisfies-conditions/
"""
from typing import List


class Solution:

    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i < m -1 and grid[i][j] != grid[i + 1][j]) or (j < n - 1 and grid[i][j] == grid[i][j + 1]):
                    return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().satisfiesConditions([[1, 0, 2], [1, 0, 2]]))
    # False
    print(Solution().satisfiesConditions([[1, 1, 1], [0, 0, 0]]))
    # False
    print(Solution().satisfiesConditions([[1], [2], [3]]))
