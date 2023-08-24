"""
 * 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
 * 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
 * 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m <= 250
 * 4、1 <= n <= 250
 * 5、grid[i][j] == 0 or 1
 * 链接：https://leetcode.cn/problems/count-servers-that-communicate/
"""
from typing import List


class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c, r = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    r[j] += 1
                    c[i] += 1
        ans = 0
        for i in range(m    ):
            for j in range(n):
                if grid[i][j] and (r[j] > 1 or c[i] > 1):
                    ans += 1
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().countServers([[1, 0], [0, 1]]))
    # 3
    print(Solution().countServers([[1, 0], [1, 1]]))
    # 4
    print(Solution().countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
