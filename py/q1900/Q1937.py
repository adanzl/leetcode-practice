"""
 * 给你一个 m x n 的整数矩阵 points （下标从 0 开始）。一开始你的得分为 0 ，你想最大化从矩阵中得到的分数。
 * 你的得分方式为：每一行 中选取一个格子，选中坐标为 (r, c) 的格子会给你的总得分 增加 points[r][c] 。
 * 然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。
 * 对于相邻行 r 和 r + 1 （其中 0 <= r < m - 1），选中坐标为 (r, c1) 和 (r + 1, c2) 的格子，
 * 你的总得分 减少 abs(c1 - c2) 。
 * 请你返回你能得到的 最大 得分。
 * abs(x) 定义为：
 * 1、如果 x >= 0 ，那么值为 x 。
 * 2、如果 x < 0 ，那么值为 -x 。
 * 链接：https://leetcode.cn/problems/maximum-number-of-points-with-cost
"""

from typing import List

#
# @lc app=leetcode.cn id=1937 lang=python3
#
# [1937] 扣分后的最大得分
#

# @lc code=start
INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        f = [0] * n
        # f[i][j] = -j + max f[i-1][k] + k (k<j)
        # f[i][j] =  j + max f[i-1][k] - k (k>j)
        for line in points:
            mx_l = []
            val = -INF
            for i in range(n):
                val = max(val, f[i] + i)
                mx_l.append(val)
            val = -INF
            for i in range(n - 1, -1, -1):
                val = max(val, f[i] - i)
                f[i] = line[i] + max(val + i, mx_l[i] - i)
        return max(f)


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().maxPoints([[1, 2, 3]]))
    # 9
    print(Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
    # 11
    print(Solution().maxPoints([[1, 5], [2, 3], [4, 2]]))
