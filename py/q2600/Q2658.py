"""
 * 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，其中下标在 (r, c) 处的整数表示：
 * 1、如果 grid[r][c] = 0 ，那么它是一块 陆地 。
 * 2、如果 grid[r][c] > 0 ，那么它是一块 水域 ，且包含 grid[r][c] 条鱼。
 * 一位渔夫可以从任意 水域 格子 (r, c) 出发，然后执行以下操作任意次：
 * 1、捕捞格子 (r, c) 处所有的鱼，或者
 * 2、移动到相邻的 水域 格子。
 * 请你返回渔夫最优策略下， 最多 可以捕捞多少条鱼。如果没有水域格子，请你返回 0 。
 * 格子 (r, c) 相邻 的格子为 (r, c + 1) ，(r, c - 1) ，(r + 1, c) 和 (r - 1, c) ，前提是相邻格子在网格图内。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10
 * 4、0 <= grid[i][j] <= 10 
 * 链接：https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/
"""
from typing import List


class Solution:

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x > m - 1 or y > n - 1 or grid[x][y] == 0:
                return 0
            ret = grid[x][y]
            grid[x][y] = 0
            ret += dfs(x + 1, y)
            ret += dfs(x - 1, y)
            ret += dfs(x, y + 1)
            ret += dfs(x, y - 1)
            return ret

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
    # 1
    print(Solution().findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
