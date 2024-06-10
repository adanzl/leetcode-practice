"""
 * 给你一个二维 boolean 矩阵 grid 。
 * 请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。
 * 注意：
 * 如果 grid 中 3 个元素满足：一个元素与另一个元素在 同一行，同时与第三个元素在 同一列 ，那么这 3 个元素称为一个 直角三角形 。
 * 这 3 个元素互相之间不需要相邻。
 * 提示：
 * 1、1 <= grid.length <= 1000
 * 2、1 <= grid[i].length <= 1000
 * 3、0 <= grid[i][j] <= 1
 * 链接：https://leetcode.cn/problems/right-triangles/
"""
from collections import defaultdict
from typing import List


class Solution:

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pos_i, pos_j = defaultdict(list), defaultdict(list)
        pre_sm_i, pre_sm_j = [0] * m, [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                pos_i[i].append(j)
                pos_j[j].append(i)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                ans += pre_sm_i[i]
                pre_sm_i[i] += len(pos_j[j]) - 1
        pre_sm_i, pre_sm_j = [0] * m, [0] * n
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0: continue
                ans += pre_sm_i[i]
                pre_sm_i[i] += len(pos_j[j]) - 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().numberOfRightTriangles([[0, 0], [0, 1], [1, 1]]))
    # 2
    print(Solution().numberOfRightTriangles([[0, 1, 0], [0, 1, 1], [0, 1, 0]]))
    # 0
    print(Solution().numberOfRightTriangles([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
    # 2
    print(Solution().numberOfRightTriangles([[1, 0, 1], [1, 0, 0], [1, 0, 0]]))
