"""
 * 链接：https://leetcode.cn/problems/delete-greatest-value-in-each-row/
"""
from typing import List


class Solution:

    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for gl in grid:
            gl.sort(reverse=True)
        for i in range(len(grid[0])):
            mx = 0
            for j in range(len(grid)):
                mx = max(mx, grid[j][i])
            ans += mx
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
    # 10
    print(Solution().deleteGreatestValue([[10]]))