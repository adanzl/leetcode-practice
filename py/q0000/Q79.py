"""
 * 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
 * 提示：
 * 1、单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 * 2、m == board.length
 * 3、n = board[i].length
 * 4、1 <= m, n <= 6
 * 5、1 <= word.length <= 15
 * 6、board 和 word 仅由大小写英文字母组成
 * 链接：https://leetcode.cn/problems/word-search/
"""
from itertools import product
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(word)
        row, col = len(board), len(board[0])

        def dfs(i, x, y, vis):
            if i == n: return True
            if word[i] != board[x][y]: return False
            if i == n - 1: return True
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
                if (nx, ny) in vis: continue
                vis.add((nx, ny))
                if dfs(i + 1, nx, ny, vis): return True
                vis.remove((nx, ny))
            return False

        return any([dfs(0, x, y, set([(x, y)])) for x, y in product(range(row), range(col))])


if __name__ == '__main__':
    # True
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    # True
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    # False
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
