"""
 * 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。
 * 从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。
 * 请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。
 * 提示：
 * 1、m == mat.length
 * 2、n = mat[i].length
 * 3、arr.length == m * n
 * 4、1 <= m, n <= 10^5
 * 5、1 <= m * n <= 10^5
 * 6、1 <= arr[i], mat[r][c] <= m * n
 * 7、arr 中的所有整数 互不相同
 * 8、mat 中的所有整数 互不相同
 * 链接：https://leetcode.cn/problems/first-completely-painted-row-or-column/
"""
from typing import List


class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        d = dict()
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        cc, rc = [0] * m, [0] * n
        for i, v in enumerate(arr):
            x, y = d[v]
            cc[x] += 1
            rc[y] += 1
            if cc[x] == n or rc[y] == m:
                return i
        return -1


if __name__ == '__main__':
    # 2
    print(Solution().firstCompleteIndex([1, 3, 4, 2], mat=[[1, 4], [2, 3]]))
    # 3
    print(Solution().firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
