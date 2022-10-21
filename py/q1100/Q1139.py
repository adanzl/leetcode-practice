"""
 * 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
 * 提示：
 * 1、1 <= grid.length <= 100
 * 2、1 <= grid[0].length <= 100
 * 3、grid[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/largest-1-bordered-square/
"""
from typing import List


class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp_r = [[0] * (n + 1) for _ in range(m + 1)]
        dp_c = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r = dp_r[i + 1][j + 1] = dp_r[i + 1][j] + 1
                    c = dp_c[j + 1][i + 1] = dp_c[j + 1][i] + 1
                    for k in range(min(r, c)):
                        if dp_r[i + 1 - k][j + 1] >= k + 1 and dp_c[j + 1 - k][i + 1] >= k + 1:
                            ans = max(ans, k + 1)
        return ans * ans


if __name__ == '__main__':
    # 1
    print(Solution().largest1BorderedSquare([[0, 1], [1, 1]]))
    # 9
    print(Solution().largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # 1
    print(Solution().largest1BorderedSquare([[1, 1, 0, 0]]))
