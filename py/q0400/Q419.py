"""
 * 给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，
 * 返回在甲板 board 上放置的 战舰 的数量。
 * 战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，
 * 其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。
 * 进阶：你可以实现一次扫描算法，并只使用 O(1) 额外空间，并且不修改 board 的值来解决这个问题吗？
 * 提示：
 * 1、m == board.length
 * 2、n == board[i].length
 * 3、1 <= m, n <= 200
 * 4、board[i][j] 是 '.' 或 'X'
 * 链接：https://leetcode.cn/problems/battleships-in-a-board/
"""

from typing import List

#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#


# @lc code=start
class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.': continue
                if (i and board[i - 1][j] == 'X') or (j and board[i][j - 1] == 'X'): continue
                ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
    # 0
    print(Solution().countBattleships([["."]]))
