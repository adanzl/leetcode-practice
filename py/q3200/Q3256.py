"""
 * 给你一个 m x n 的二维整数数组 board ，它表示一个国际象棋棋盘，其中 board[i][j] 表示格子 (i, j) 的 价值 。
 * 处于 同一行 或者 同一列 车会互相 攻击 。你需要在棋盘上放三个车，确保它们两两之间都 无法互相攻击 。
 * 请你返回满足上述条件下，三个车所在格子 值 之和 最大 为多少。
 * 提示：
 * 1、3 <= m == board.length <= 100
 * 2、3 <= n == board[i].length <= 100
 * 3、-10^9 <= board[i][j] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-i/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        dp0 = [[0] * (n) for _ in range(m)]  # left up
        dp1 = [[0] * (n) for _ in range(m)]  # right up
        dp2 = [[0] * (n) for _ in range(m)]  # left down
        dp3 = [[0] * (n) for _ in range(m)]  # right down
        f_row0 = [[0] * (n) for _ in range(m)]  # l->r
        f_row1 = [[0] * (n) for _ in range(m)]  # r->l
        f_col0 = [[0] * (n) for _ in range(m)]  # u->d
        f_col1 = [[0] * (n) for _ in range(m)]  # d->u

        dp0[0][0] = board[0][0]
        dp1[0][-1] = board[0][-1]
        dp2[-1][0] = board[-1][0]
        dp3[-1][-1] = board[-1][-1]
        for i in range(m):
            f_row0[i][0] = board[i][0]
            f_row1[i][-1] = board[i][-1]

        for j in range(n):
            f_col0[0][j] = board[0][j]
            f_col1[-1][j] = board[-1][j]
        for i in range(1, m):
            dp0[i][0] = max(board[i][0], dp0[i - 1][0])
            dp1[i][-1] = max(board[i][-1], dp1[i - 1][-1])
            dp2[m - 1 - i][0] = max(board[m - 1 - i][0], dp2[m - i][0])
            dp3[m - 1 - i][-1] = max(board[m - 1 - i][-1], dp3[m - i][-1])
            f_col0[i][0] = max(f_col0[i - 1][0], board[i][0])
            f_col1[m - 1 - i][0] = max(f_col1[m - i][0], board[m - 1 - i][0])
        for j in range(1, n):
            dp0[0][j] = max(dp0[0][j - 1], board[0][j])
            dp1[0][n - 1 - j] = max(dp1[0][n - j], board[0][n - 1 - j])
            dp2[-1][j] = max(dp2[-1][j - 1], board[-1][j])
            dp3[-1][n - 1 - j] = max(dp3[-1][n - j], board[-1][n - 1 - j])
            f_row0[0][j] = max(f_row0[0][j - 1], board[0][j])
            f_row1[0][n - 1 - j] = max(f_row1[0][n - j], board[0][n - 1 - j])

        for i in range(1, m):

            for j in range(1, n):
                dp0[i][j] = max(dp0[i - 1][j], dp0[i][j - 1], board[i][j])
                dp1[i][n - 1 - j] = max(dp1[i - 1][n - 1 - j], dp1[i][n - j], board[i][n - 1 - j])
                dp2[-1 - i][j] = max(dp2[-1 - i][j - 1], dp2[-i][j], board[-1 - i][j])
                dp3[-1 - i][-1 - j] = max(dp3[-1 - i][-j], dp3[-i][-1 - j], board[-1 - i][-1 - j])
                f_row0[i][j] = max(f_row0[i][j - 1], board[i][j])
                f_row1[i][n - 1 - j] = max(f_row1[i][n - j], board[i][n - 1 - j])
                f_col0[i][j] = max(f_col0[i - 1][j], board[i][j])
                f_col1[m - 1 - i][j] = max(f_col1[m - i][j], board[m - 1 - i][j])

        ans = -INF
        for i in range(m):
            for j in range(n):
                # 切割成四个区域 选两个区域选1个
                if not ((i == 0 or i == m - 1) and (j == 0 or j == n - 1)):
                    v0 = dp0[i - 1][j - 1] if i and j else -INF  # left up
                    v1 = dp1[i - 1][j + 1] if i and j < n - 1 else -INF  # right up
                    v2 = dp2[i + 1][j - 1] if i < m - 1 and j else -INF  # left down
                    v3 = dp3[i + 1][j + 1] if i < m - 1 and j < n - 1 else -INF  # right down
                    # 对角线
                    val = max(v0 + v3, v1 + v2)

                    # 同侧 4 种
                    # left v0 v2
                    for k in range(j - 1, -1, -1):
                        if i > 0:
                            # 先取up
                            val = max(val, f_col0[i - 1][k] + (dp2[i + 1][k - 1] if i < m - 1 and k else -INF))
                        if i < m - 1:
                            # 先取down
                            val = max(val, f_col1[i + 1][k] + (dp0[i - 1][k - 1] if i and k else -INF))
                    # right v1 v3
                    for k in range(j + 1, n):
                        if i > 0:
                            # 先取up
                            val = max(val, f_col0[i - 1][k] + (dp3[i + 1][k + 1] if i < m - 1 and k < n - 1 else -INF))
                        if i < m - 1:
                            # 先取down
                            val = max(val, f_col1[i + 1][k] + (dp1[i - 1][k + 1] if i and k < n - 1 else -INF))
                    # up v0 v1
                    for k in range(i - 1, -1, -1):
                        if j > 0:
                            # 先取left
                            val = max(val, f_row0[k][j - 1] + (dp1[k - 1][j + 1] if k and j < n - 1 else -INF))
                        if j < n - 1:
                            # 先取right
                            val = max(val, f_row1[k][j + 1] + (dp0[k - 1][j - 1] if k and j else -INF))
                    # down v2 v3
                    for k in range(i + 1, m):
                        if j > 0:
                            # 先取left
                            val = max(val, f_row0[k][j - 1] + (dp3[k + 1][j + 1] if k < m - 1 and j < n - 1 else -INF))
                        if j < n - 1:
                            # 先取right
                            val = max(val, f_row1[k][j + 1] + (dp2[k + 1][j - 1] if k < m - 1 and j else -INF))
                    ans = max(ans, val + board[i][j])
        return ans


if __name__ == '__main__':
    # 243
    print(Solution().maximumValueSum([[-45, 64, 59, 97, -25], [64, 33, 49, 76, 70], [17, 27, -50, -18, 32],
                                      [36, -67, -70, 25, 82], [20, 28, -77, 62, 51]]))
    # 173
    print(Solution().maximumValueSum([[-12, 70, -48, -74], [-71, -75, 63, -67], [-46, 81, 4, -86], [29, -51, -51, 16]]))
    # 15
    print(Solution().maximumValueSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # 4
    print(Solution().maximumValueSum([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]))
    # 3
    print(Solution().maximumValueSum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
