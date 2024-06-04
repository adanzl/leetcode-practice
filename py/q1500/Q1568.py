"""
 * 给你一个大小为 m x n ，由若干 0 和 1 组成的二维网格 grid ，其中 1 表示陆地， 0 表示水。
 * 岛屿 由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
 * 如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
 * 一天内，可以将 任何单个 陆地单元（1）更改为水单元（0）。
 * 返回使陆地分离的最少天数。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 30
 * 4、grid[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/minimum-number-of-days-to-disconnect-island/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=1568 lang=python3
#
# [1568] 使陆地分离的最少天数
#


# @lc code=start
class Solution:

    def minDays(self, grid: List[List[int]]) -> int:
        # 任何情况陆地都是有角的，删除角即可
        # 首先，判断输入本身就是分离的。
        # 其次，暴力枚举删除输入中的一个 1，然后判断是否分离。
        # 再其次，直接返回 2
        m, n = len(grid), len(grid[0])

        def find(parent, x):
            r = x
            while parent[r] != r:
                r = parent[r]
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r

        def check():
            parent = [i for i in range(n * m)]
            cnt = m * n
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        cnt -= 1
                        continue
                    r0 = find(parent, i * n + j)
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                            r1 = find(parent, nx * n + ny)
                            if r0 != r1:
                                parent[r1] = r0
                                cnt -= 1
                    if cnt == 0:
                        return True
            return cnt != 1

        if check(): return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                grid[i][j] = 0
                if check(): return 1
                grid[i][j] = 1

        return 2


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().minDays([[1, 1]]))
    # 2
    print(Solution().minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    # 2
    print(Solution().minDays([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]))
