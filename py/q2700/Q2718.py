"""
 * 给你一个整数 n 和一个下标从 0 开始的 二维数组 queries ，其中 queries[i] = [type_i, index_i, val_i] 。
 * 一开始，给你一个下标从 0 开始的 n x n 矩阵，所有元素均为 0 。每一个查询，你需要执行以下操作之一：
 * 1、如果 type_i == 0 ，将第 index_i 行的元素全部修改为 val_i ，覆盖任何之前的值。
 * 2、如果 type_i == 1 ，将第 index_i 列的元素全部修改为 val_i ，覆盖任何之前的值。
 * 请你执行完所有查询以后，返回矩阵中所有整数的和。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、1 <= queries.length <= 5 * 10^4
 * 3、queries[i].length == 3
 * 4、0 <= type_i <= 1
 * 5、0 <= index_i < n
 * 6、0 <= val_i <= 10^5
 * 链接：https://leetcode.cn/problems/sum-of-matrix-after-queries/
"""
from typing import List


class Solution:

    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row, col = set(), set()
        ans = 0
        for i in range(len(queries) - 1, -1, -1):
            t, ii, v = queries[i]
            if t == 0:
                if ii in row:
                    continue
                row.add(ii)
                ans += v * (n - len(col))
            else:
                if ii in col:
                    continue
                col.add(ii)
                ans += v * (n - len(row))
        return ans


if __name__ == '__main__':
    # 23
    print(Solution().matrixSumQueries(3, queries=[[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]))
    # 17
    print(Solution().matrixSumQueries(3, queries=[[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]))