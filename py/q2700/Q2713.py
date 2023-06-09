"""
 * 给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。
 * 从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。
 * 你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。
 * 请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。
 * 返回一个表示可访问单元格最大数量的整数。
 * 提示：
 * 1、m == mat.length 
 * 2、n == mat[i].length 
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 10^5
 * 5、-10^5 <= mat[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/
"""
from collections import defaultdict
from typing import List


class Solution:

    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置

        ans = 0
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda p: p[0]):
            # 先把最大值算出来，再更新 row_max 和 col_max
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            ans = max(ans, max(mx))
            for (i, j), f in zip(pos, mx):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxIncreasingCells([[3, 1], [3, 4]]))
    # 4
    print(Solution().maxIncreasingCells([[3, 1, 6], [-9, 5, 7]]))
    # 4
    print(Solution().maxIncreasingCells([[-8, 4, 9, -1]]))
    # 1
    print(Solution().maxIncreasingCells([[1, 1], [1, 1]]))
