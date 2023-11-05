"""
 * 一场比赛中共有 n 支队伍，按从 0 到  n - 1 编号。
 * 给你一个下标从 0 开始、大小为 n * n 的二维布尔矩阵 grid 。
 * 对于满足 0 <= i, j <= n - 1 且 i != j 的所有 i, j ：
 * 1、如果 grid[i][j] == 1，那么 i 队比 j 队 强 
 * 2、否则，j 队比 i 队 强 。
 * 在这场比赛中，如果不存在某支强于 a 队的队伍，则认为 a 队将会是 冠军 。
 * 返回这场比赛中将会成为冠军的队伍。
 * 提示：
 * 1、n == grid.length
 * 2、n == grid[i].length
 * 3、2 <= n <= 100
 * 4、grid[i][j] 的值为 0 或 1
 * 5、对于满足 i != j 的所有 i, j ，grid[i][j] != grid[j][i] 均成立
 * 6、生成的输出满足：如果 a 队比 b 队强，b 队比 c 队强，那么 a 队比 c 队强
 * 链接：https://leetcode.cn/problems/find-champion-i/
"""
from typing import List


class Solution:

    def findChampion(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ss = set([i for i in range(n)])
        for i in range(m):
            for j in range(i + 1, n):
                if grid[i][j]:
                    ss.discard(j)
                else:
                    ss.discard(i)
        return min(ss)


if __name__ == '__main__':
    # 0
    print(Solution().findChampion([[0, 1], [0, 0]]))
    # 1
    print(Solution().findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
