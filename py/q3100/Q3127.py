"""
 * 给你一个二维 3 x 3 的矩阵 grid ，每个格子都是一个字符，要么是 'B' ，要么是 'W' 。字符 'W' 表示白色，字符 'B' 表示黑色。
 * 你的任务是改变 至多一个 格子的颜色，使得矩阵中存在一个 2 x 2 颜色完全相同的正方形。
 * 如果可以得到一个相同颜色的 2 x 2 正方形，那么返回 true ，否则返回 false 。
 * 提示：
 * 1、grid.length == 3
 * 2、grid[i].length == 3
 * 3、grid[i][j] 要么是 'W' ，要么是 'B' 。
 * 链接：https://leetcode.cn/problems/make-a-square-with-the-same-color/
"""
from typing import List


class Solution:

    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def check():
            for i in range(2):
                for j in range(2):
                    if grid[i][j] == grid[i][j + 1] and \
                        grid[i][j + 1] == grid[i + 1][j + 1] and \
                            grid[i+ 1][j + 1] == grid[i+1][j ]:
                        return True
            return False

        if check(): return True
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'B':
                    grid[i][j] = 'W'
                    if check(): return True
                    grid[i][j] = 'B'
                if grid[i][j] == 'W':
                    grid[i][j] = 'B'
                    if check(): return True
                    grid[i][j] = 'W'

        return False


if __name__ == '__main__':
    # True
    print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
    # False
    print(Solution().canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
    # True
    print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]))
