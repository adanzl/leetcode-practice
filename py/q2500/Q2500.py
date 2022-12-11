"""
 * 链接：https://leetcode.cn/problems/delete-greatest-value-in-each-row/
"""
from typing import List


class Solution:

    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            row.sort()
        # 遍历列
        for col in zip(*grid):
            ans += max(col)
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
    # 10
    print(Solution().deleteGreatestValue([[10]]))