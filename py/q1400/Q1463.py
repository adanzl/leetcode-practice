"""
 * 给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。
 * 1、你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。
 * 2、请你按照如下规则，返回两个机器人能收集的最多樱桃数目：
 * 3、从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
 * 4、当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
 * 5、当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
 * 6、两个机器人在任意时刻都不能移动到 grid 外面。
 * 7、两个机器人最后都要到达 grid 最底下一行。
 * 提示：
 * 1、rows == grid.length
 * 2、cols == grid[i].length
 * 3、2 <= rows, cols <= 70
 * 4、0 <= grid[i][j] <= 100 
 * 链接：https://leetcode.cn/problems/cherry-pickup-ii/
"""
from functools import cache
from typing import List


class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        @cache
        def f(i0, i1, r):
            if i0 < 0 or i0 > col - 1 or i1 < 0 or i1 > col - 1: return 0
            ret = grid[r][i0] if i0 == i1 else (grid[r][i0] + grid[r][i1])
            if r == row - 1: return ret
            v = 0
            for i in [i0 - 1, i0, i0 + 1]:
                for j in [i1 - 1, i1, i1 + 1]:
                    v = max(v, f(i, j, r + 1))
            return ret + v

        return f(0, col - 1, 0)


if __name__ == '__main__':
    # 28
    print(Solution().cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0], [1, 0, 2, 3, 0, 0, 6]]))
    # 22
    print(Solution().cherryPickup([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))
    # 4
    print(Solution().cherryPickup([[1, 1], [1, 1]]))
