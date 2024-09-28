"""
 * 给你两个字符串 coordinate1 和 coordinate2，代表 8 x 8 国际象棋棋盘上的两个方格的坐标。
 * 以下是棋盘的参考图。
 * 如果这两个方格颜色相同，返回 true，否则返回 false。
 * 坐标总是表示有效的棋盘方格。坐标的格式总是先字母（表示列），再数字（表示行）。
 * 提示：
 * 1、coordinate1.length == coordinate2.length == 2
 * 2、'a' <= coordinate1[0], coordinate2[0] <= 'h'
 * 3、'1' <= coordinate1[1], coordinate2[1] <= '8'
 * 链接：https://leetcode.cn/problems/check-if-two-chessboard-squares-have-the-same-color
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x0, y0 = ord(coordinate1[0]) - ord('a'), int(coordinate1[1]) - 1
        x1, y1 = ord(coordinate2[0]) - ord('a'), int(coordinate2[1]) - 1
        return (x0 + y0) & 1 == (x1 + y1) & 1


if __name__ == '__main__':
    # True
    print(Solution().checkTwoChessboards("a1", coordinate2="c3"))
    # False
    print(Solution().checkTwoChessboards("a1", coordinate2="h3"))
