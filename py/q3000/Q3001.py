"""
 * 现有一个下标从 0 开始的 8 x 8 棋盘，上面有 3 枚棋子。
 * 给你 6 个整数 a 、b 、c 、d 、e 和 f ，其中：
 * 1、(a, b) 表示白色车的位置。
 * 2、(c, d) 表示白色象的位置。
 * 3、(e, f) 表示黑皇后的位置。
 * 假定你只能移动白色棋子，返回捕获黑皇后所需的最少移动次数。
 * 请注意：
 * 1、车可以向垂直或水平方向移动任意数量的格子，但不能跳过其他棋子。
 * 2、象可以沿对角线方向移动任意数量的格子，但不能跳过其他棋子。
 * 3、如果车或象能移向皇后所在的格子，则认为它们可以捕获皇后。
 * 4、皇后不能移动。
 * 提示：
 * 1、1 <= a, b, c, d, e, f <= 8
 * 2、两枚棋子不会同时出现在同一个格子上。
 * 链接：https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/
"""


class Solution:

    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if e == a and (c != e or (d - b) * (d - f) >= 0): return 1
        if f == b and (d != f or (c - a) * (c - e) >= 0): return 1
        if abs(c - e) == abs(d - f):
            if abs(a - c) != abs(b - d):
                # 相无法抵达车
                return 1
            if (c - a) * (c - e) * (d - b) * (d - f) <= 0:
                # 车和后不在一边
                return 1
            if (e - a) * (e - c) < 0 and (f - b) * (f - d) < 0:
                # 后在中间
                return 1
            if (c - a) * (c - e) < 0 and (d - b) * (d - f) < 0:
                # 相在中间
                return 1
        return 2


if __name__ == '__main__':
    # 2
    print(Solution().minMovesToCaptureTheQueen(3, 1, 2, 1, 1, 1))
    # 1
    print(Solution().minMovesToCaptureTheQueen(1, 8, 7, 2, 6, 1))
    # 1
    print(Solution().minMovesToCaptureTheQueen(4, 3, 3, 4, 2, 5))
    # 2
    print(Solution().minMovesToCaptureTheQueen(1, 1, 1, 4, 1, 8))
    # 2
    print(Solution().minMovesToCaptureTheQueen(4, 3, 3, 4, 5, 2))
    # 2
    print(Solution().minMovesToCaptureTheQueen(1, b=1, c=8, d=8, e=2, f=3))
    # 1
    print(Solution().minMovesToCaptureTheQueen(5, b=3, c=3, d=4, e=5, f=2))
