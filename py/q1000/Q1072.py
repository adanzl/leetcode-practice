"""
 * 给定 m x n 矩阵 matrix 。
 * 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
 * 返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 300
 * 4、matrix[i][j] == 0 或 1
 * 链接：https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/
"""
from collections import Counter
from typing import List


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] ^= 1
            cnt[tuple(row)] += 1
        return cnt.most_common(1)[0][1]


if __name__ == '__main__':
    # 1
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]))
    # 2
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
    # 2
    print(Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
