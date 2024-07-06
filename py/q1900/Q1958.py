"""
 * 给你一个下标从 0 开始的 8 x 8 网格 board ，其中 board[r][c] 表示游戏棋盘上的格子 (r, c) 。
 * 棋盘上空格用 '.' 表示，白色格子用 'W' 表示，黑色格子用 'B' 表示。
 * 游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。
 * 但是，合法 操作必须满足：涂色后这个格子是 好线段的一个端点 （好线段可以是水平的，竖直的或者是对角线）。
 * 好线段 指的是一个包含 三个或者更多格子（包含端点格子）的线段，线段两个端点格子为 同一种颜色 ，
 * 且中间剩余格子的颜色都为 另一种颜色 （线段上不能有任何空格子）。你可以在下图找到好线段的例子：
 * 给你两个整数 rMove 和 cMove 以及一个字符 color ，表示你正在执行操作的颜色（白或者黑），
 * 如果将格子 (rMove, cMove) 变成颜色 color 后，是一个 合法 操作，那么返回 true ，如果不是合法操作返回 false 。
 * 提示：
 * 1、board.length == board[r].length == 8
 * 2、0 <= rMove, cMove < 8
 * 3、board[rMove][cMove] == '.'
 * 4、color 要么是 'B' 要么是 'W' 。
 * 链接：https://leetcode.cn/problems/check-if-move-is-legal
"""

from typing import List

#
# @lc app=leetcode.cn id=1958 lang=python3
#
# [1958] 检查操作是否合法
#


# @lc code=start
class Solution:

    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        for dx, dy in [
            [1, 0],  # b
            [-1, 0],  # t
            [0, -1],  # l
            [0, 1],  # r
            [1, -1],  # lb
            [1, 1],  # rb
            [-1, -1],  # lt
            [-1, 1],  # rt
        ]:
            x, y = rMove + dx, cMove + dy
            step = 0
            while 0 <= x < m and 0 <= y < n:
                if board[x][y] == '.': break
                if board[x][y] == color:
                    if step == 0:
                        break
                    else:
                        return True
                step += 1
                x, y = x + dx, y + dy

        return False


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().checkMove([[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                                [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                                ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."],
                                [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]],
                               rMove=4,
                               cMove=3,
                               color="B"))
    # False
    print(Solution().checkMove([[".", ".", ".", ".", ".", ".", ".", "."], [".", "B", ".", ".", "W", ".", ".", "."],
                                [".", ".", "W", ".", ".", ".", ".", "."], [".", ".", ".", "W", "B", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "B", "W", ".", "."],
                                [".", ".", ".", ".", ".", ".", "W", "."], [".", ".", ".", ".", ".", ".", ".", "B"]],
                               rMove=4,
                               cMove=4,
                               color="W"))
