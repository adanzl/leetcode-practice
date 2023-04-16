"""
 * 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。矩阵中某一列的宽度是这一列数字的最大 字符串长度 。
 * 比方说，如果 grid = [[-10], [3], [12]] ，那么唯一一列的宽度是 3 ，因为 -10 的字符串长度为 3 。
 * 请你返回一个大小为 n 的整数数组 ans ，其中 ans[i] 是第 i 列的宽度。
 * 一个有 len 个数位的整数 x ，如果是非负数，那么 字符串长度 为 len ，否则为 len + 1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 100
 * 4、-10^9 <= grid[r][c] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid/
"""
from typing import List


class Solution:

    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for i in range(n):
            for j in range(m):
                ans[i] = max(ans[i], len(str(grid[j][i])))
        return ans


if __name__ == '__main__':
    # [3]
    print(Solution().findColumnWidth([[1], [22], [333]]))
    # [3,1,2]
    print(Solution().findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))
