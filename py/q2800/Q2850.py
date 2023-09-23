"""
 * 给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。
 * 网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。
 * 每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。
 * 请你返回每个格子恰好有一个石头的 最少移动次数 。
 * 提示：
 * 1、grid.length == grid[i].length == 3
 * 2、0 <= grid[i][j] <= 9
 * 3、grid 中元素之和为 9 。
 * 链接：https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/
"""
from functools import cache
from typing import List
#
# @lc app=leetcode.cn id=2850 lang=python3
#

# @lc code=start


class Solution:

    def minimumMoves(self, grid: List[List[int]]) -> int:

        @cache
        def f(gt, s):
            ret = 10**32
            g = list(gt)
            ids = []
            for i in range(3):
                for j in range(3):
                    if g[i * 3 + j] > 1:
                        ids.append((i, j))
            if len(ids) == 0:
                return s
            for i in range(3):
                for j in range(3):
                    if g[i * 3 + j] == 0:
                        g[i * 3 + j] = 1
                        for x1, y1 in ids:
                            g[x1 * 3 + y1] -= 1
                            ret = min(ret, f(tuple(g), s + abs(i - x1) + abs(j - y1)))
                            g[x1 * 3 + y1] += 1
                        g[i * 3 + j] = 0
            return ret

        return f(tuple([grid[i][j] for i in range(3) for j in range(3)]), 0)


# @lc code=end

if __name__ == '__main__':
    # 10
    print(Solution().minimumMoves([[3, 0, 0], [4, 1, 0], [1, 0, 0]]))
    # 4
    print(Solution().minimumMoves([[1, 2, 2], [1, 1, 0], [0, 1, 1]]))
    # 6
    print(Solution().minimumMoves([[0, 2, 3], [2, 0, 1], [0, 1, 0]]))
    # 3
    print(Solution().minimumMoves([[1, 1, 0], [1, 1, 1], [1, 2, 1]]))
    # 4
    print(Solution().minimumMoves([[1, 3, 0], [1, 0, 0], [1, 0, 3]]))
