"""
 * 大小为 n x n 的矩阵 grid 中有一条蛇。蛇可以朝 四个可能的方向 移动。
 * 矩阵中的每个单元格都使用位置进行标识： grid[i][j] = (i * n) + j。
 * 蛇从单元格 0 开始，并遵循一系列命令移动。
 * 给你一个整数 n 表示 grid 的大小，另给你一个字符串数组 commands，其中包括 "UP"、"RIGHT"、"DOWN" 和 "LEFT"。
 * 题目测评数据保证蛇在整个移动过程中将始终位于 grid 边界内。
 * 返回执行 commands 后蛇所停留的最终单元格的位置。
 * 提示：
 * 1、2 <= n <= 10
 * 2、1 <= commands.length <= 100
 * 3、commands 仅由 "UP"、"RIGHT"、"DOWN" 和 "LEFT" 组成。
 * 4、生成的测评数据确保蛇不会移动到矩阵的边界外。
 * 链接：https://leetcode.cn/problems/snake-in-matrix/description/
"""
from typing import List


class Solution:

    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for c in commands:
            if c == "UP":
                ans -= n
            elif c == "DOWN":
                ans += n
            elif c == "RIGHT":
                ans += 1
            else:
                ans -= 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().finalPositionOfSnake(2, commands=["RIGHT", "DOWN"]))
    # 1
    print(Solution().finalPositionOfSnake(3, commands=["DOWN", "RIGHT", "UP"]))
