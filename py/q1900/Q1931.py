"""
 * 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。
 * 请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
 * 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。
 * 返回网格涂色的方法数。因为答案可能非常大， 返回 对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、1 <= m <= 5
 * 2、1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/
"""

from functools import cache

#
# @lc app=leetcode.cn id=1931 lang=python3
#
# [1931] 用三种不同颜色为网格涂色
#

# @lc code=start
import sys

sys.setrecursionlimit(10**4)
g_marks = [[], [], [], [], []]


def f(idx, num):
    if idx == 5: return
    for nn in '123':
        if num and num[-1] == nn: continue
        g_marks[idx].append(num + nn)
        f(idx + 1, num + nn)


f(0, '')


class Solution:

    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        marks = g_marks[m - 1]

        @cache
        def dfs(idx, col_mark):
            if idx == n: return 1
            ret = 0
            for nx_mark in marks:
                for a, b in zip(col_mark, nx_mark):
                    if a == b:
                        break
                else:
                    ret += dfs(idx + 1, nx_mark)
                    ret %= MOD
            return ret

        return dfs(0, '')


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().colorTheGrid(1, 1))
    # 6
    print(Solution().colorTheGrid(1, 2))
    # 580986
    print(Solution().colorTheGrid(5, 5))
    # 408208448
    print(Solution().colorTheGrid(5, 1000))
