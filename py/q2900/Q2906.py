"""
 * 给你一个下标从 0 开始、大小为 n * m 的二维整数矩阵 grid ，定义一个下标从 0 开始、大小为 n * m 的的二维矩阵 p。
 * 如果满足以下条件，则称 p 为 grid 的 乘积矩阵 ：
 * 对于每个元素 p[i][j] ，它的值等于除了 grid[i][j] 外所有元素的乘积。乘积对 12345 取余数。
 * 返回 grid 的乘积矩阵。
 * 提示：
 * 1、1 <= n == grid.length <= 10^5
 * 2、1 <= m == grid[i].length <= 10^5
 * 3、2 <= n * m <= 10^5
 * 4、1 <= grid[i][j] <= 10^9
 * 链接：https://leetcode.cn/problems/construct-product-matrix/
"""
from typing import List


class Solution:

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MOD = 12345
        ans = [[0] * n for _ in range(m)]
        suf = [[0] * n for _ in range(m)]
        suf[m - 1][n - 1] = grid[-1][-1]
        for ii in range(m * n - 2, -1, -1):
            i, j = divmod(ii, n)
            pi, pj = divmod(ii + 1, n)
            suf[i][j] = suf[pi][pj] * grid[i][j] % MOD
        pre = 1
        for ii in range(m * n - 1):
            i, j = divmod(ii, n)
            si, sj = divmod(ii + 1, n)
            ans[i][j] = pre * suf[si][sj] % MOD
            pre = pre * grid[i][j] % MOD
        ans[-1][-1] = pre
        return ans


if __name__ == '__main__':
    # [[7005,8670,11820],[5805,7005,4170],[4155,11010,7005],[9675,6450,4155],[4170,7005,8670],[4170,5805,11820]]
    print(Solution().constructProductMatrix([[3, 1, 7], [10, 3, 8], [11, 12, 3], [6, 9, 11], [8, 3, 1], [8, 10, 7]]))
    # [[24,12],[8,6]]
    print(Solution().constructProductMatrix([[1, 2], [3, 4]]))
    # [[2],[0],[0]]
    print(Solution().constructProductMatrix([[12345], [2], [1]]))
