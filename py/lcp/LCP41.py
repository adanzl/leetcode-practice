"""
 * 在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."。
 * 当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。
 * 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。
 * 若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。
 * 注意：
 * 1、若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 继续 翻转白棋
 * 2、输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置
 * 提示：
 * 1、1 <= chessboard.length, chessboard[i].length <= 8
 * 2、chessboard[i] 仅包含 "."、"O" 和 "X"
 * 链接：https://leetcode.cn/problems/fHi6rV/
"""
from typing import Deque, List


class Solution:

    def flipChess(self, chessboard: List[str]) -> int:

        def bfs(i: int, j: int) -> int:
            q = Deque([(i, j)])
            g = [list(row) for row in chessboard]
            cnt = 0
            while q:
                i, j = q.popleft()
                for a, b in dirs:
                    x, y = i + a, j + b
                    while 0 <= x < m and 0 <= y < n and g[x][y] == "O":
                        x, y = x + a, y + b
                    if 0 <= x < m and 0 <= y < n and g[x][y] == "X":
                        x, y = x - a, y - b
                        cnt += max(abs(x - i), abs(y - j))
                        while x != i or y != j:
                            g[x][y] = "X"
                            q.append((x, y))
                            x, y = x - a, y - b
            return cnt

        m, n = len(chessboard), len(chessboard[0])
        dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]
        return max(bfs(i, j) for i in range(m) for j in range(n) if chessboard[i][j] == ".")


if __name__ == '__main__':
    # 4
    print(Solution().flipChess([".......", ".......", ".......", "X......", ".O.....", "..O....", "....OOX"]))
    # 1
    print(Solution().flipChess(["....X.", "....X.", "XOOO..", "......", "......"]))
    # 2
    print(Solution().flipChess([".X.", ".O.", "XO."]))
