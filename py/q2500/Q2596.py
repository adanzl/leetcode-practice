"""
 * 骑士在一张 n x n 的棋盘上巡视。在有效的巡视方案中，骑士会从棋盘的 左上角 出发，并且访问棋盘上的每个格子 恰好一次 。
 * 给你一个 n x n 的整数矩阵 grid ，由范围 [0, n * n - 1] 内的不同整数组成，其中 grid[row][col] 表示单元格 (row, col) 是骑士访问的第 grid[row][col] 个单元格。
 * 骑士的行动是从下标 0 开始的。
 * 如果 grid 表示了骑士的有效巡视方案，返回 true 否则返回 false。
 * 注意，骑士行动时可以垂直移动两个格子且水平移动一个格子，或水平移动两个格子且垂直移动一个格子。下图展示了骑士从某个格子出发可能的八种行动路线。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、3 <= n <= 7
 * 3、0 <= grid[row][col] < n * n
 * 4、grid 中的所有整数 互不相同
 * 链接：https://leetcode.cn/problems/check-knight-tour-configuration/
"""
from typing import List


class Solution:

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        pos: dict[int, List[int]] = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pos[grid[i][j]] = [i, j]
        cur_pos, cur_idx, = [0, 0], 0
        while cur_idx < len(grid)**2 - 1:
            nx_idx = cur_idx + 1
            if nx_idx not in pos: return False
            nx_pos = pos[nx_idx]
            v1, v2 = abs(nx_pos[0] - cur_pos[0]), abs(nx_pos[1] - cur_pos[1])
            if not (v1 == 2 and v2 == 1) and not (v1 == 1 and v2 == 2):
                return False
            cur_idx = nx_idx
            cur_pos = nx_pos
        return True


if __name__ == '__main__':
    # True
    print(Solution().checkValidGrid([[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))
    # False
    print(Solution().checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))
