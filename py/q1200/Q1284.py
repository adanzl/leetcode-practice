"""
 * 给你一个 m x n 的二进制矩阵 mat。每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。
 * 如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。
 * 请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。
 * 二进制矩阵 的每一个格子要么是 0 要么是 1 。
 * 全零矩阵 是所有格子都为 0 的矩阵。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[0].length
 * 3、1 <= m <= 3
 * 4、1 <= n <= 3
 * 5、mat[i][j] 是 0 或 1 。
 * 链接：https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
"""

from typing import List

#
# @lc app=leetcode.cn id=1284 lang=python3
#
# [1284] 转化为全零矩阵的最少反转次数
#


# @lc code=start
class Solution:

    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        vv = 0
        for i in range(m):
            for j in range(n):
                vv = (vv << 1) + mat[i][j]
        if vv == 0: return 0
        ans = [-1] * (1 << m * n)
        ans[0] = 0
        q = [0]
        d = 0
        while q:
            t = []
            for v in q:
                for s in range(m * n):
                    i, j = divmod(s, n)
                    nv = v ^ (1 << s)
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                        nv ^= 1 << (ni * n + nj)
                    if ans[nv] == -1:
                        ans[nv] = d + 1
                        if vv == nv: return d + 1
                        t.append(nv)
            d += 1
            q = t
        return -1


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().minFlips([[1, 1, 1], [1, 0, 1], [0, 0, 0]]))
    # 3
    print(Solution().minFlips([[0, 0], [0, 1]]))
    # 0
    print(Solution().minFlips([[0]]))
    # -1
    print(Solution().minFlips([[1, 0, 0], [1, 0, 0]]))
