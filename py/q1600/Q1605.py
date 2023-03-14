"""
 * 给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和， colSum[j] 是第 j 列元素的和。
 * 换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。
 * 请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。
 * 请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。
 * 提示：
 * 1、1 <= rowSum.length, colSum.length <= 500
 * 2、0 <= rowSum[i], colSum[i] <= 10^8
 * 3、sum(rowSum) == sum(colSum)
 * 链接：https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/
"""
from typing import List


class Solution:

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        mat = [[0] * n for _ in range(m)]
        for i, rs in enumerate(rowSum):
            for j, cs in enumerate(colSum):
                mat[i][j] = x = min(rs, cs)
                rs -= x
                colSum[j] -= x
        return mat


if __name__ == '__main__':
    # [[3,0], [1,7]]
    print(Solution().restoreMatrix([3, 8], colSum=[4, 7]))
    # [[0,5,0], [6,1,0], [2,0,8]]
    print(Solution().restoreMatrix([5, 7, 10], colSum=[8, 6, 8]))
    # [[0,9,5], [6,0,3]]
    print(Solution().restoreMatrix([14, 9], colSum=[6, 9, 8]))
    # [[1], [0]]
    print(Solution().restoreMatrix([1, 0], colSum=[1]))
    # [[0]]
    print(Solution().restoreMatrix([0], colSum=[0]))
