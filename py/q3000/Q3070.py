"""
 * 给你一个下标从 0 开始的整数矩阵 grid 和一个整数 k。返回包含 grid 左上角元素、元素和小于或等于 k 的 子矩阵 的数目。
 * 提示：
 * 1、m == grid.length 
 * 2、n == grid[i].length
 * 3、1 <= n, m <= 1000 
 * 4、0 <= grid[i][j] <= 1000
 * 5、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/
"""
from typing import List


class Solution:

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        l_pre = [0] * n
        for i in range(m):
            sm = 0
            for j in range(n):
                l_pre[j] += grid[i][j]
                sm += l_pre[j]
                if sm <= k:
                    ans += 1
                else:
                    break
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().countSubmatrices([[7, 6, 3], [6, 6, 1]], k=18))
    # 6
    print(Solution().countSubmatrices([[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20))
    #
    # print(Solution().countSubmatrices())
