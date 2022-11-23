"""
 * 给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
 * 同时给你迷宫的入口 entrance ，用 entrance = [entrance_row, entrance_col] 表示你一开始所在格子的行和列。
 * 每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。
 * 出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。
 * 请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。
 * 提示：
 * 1、maze.length == m
 * 2、maze[i].length == n
 * 3、1 <= m, n <= 100
 * 4、maze[i][j] 要么是 '.' ，要么是 '+' 。
 * 5、entrance.length == 2
 * 6、0 <= entrance_row < m
 * 7、0 <= entrance_col < n
 * 8、entrance 一定是空格子。
 * 链接：https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/
"""
from typing import List


class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = 0
        m, n = len(maze), len(maze[0])
        vis = set([(entrance[0], entrance[1])])
        q = [entrance]
        while q:
            tmp = q
            q = []
            for x, y in tmp:
                for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx > m - 1 or ny > n - 1:
                        if x == entrance[0] and y == entrance[1]: continue
                        return ans
                    if maze[nx][ny] == '+': continue
                    if (nx, ny) in vis: continue
                    vis.add((nx, ny))
                    q.append([nx, ny])
            ans += 1
        return -1


if __name__ == '__main__':
    # 2
    print(Solution().nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]))
    # 1
    print(Solution().nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2]))
    # -1
    print(Solution().nearestExit([[".", "+"]], entrance=[0, 0]))
