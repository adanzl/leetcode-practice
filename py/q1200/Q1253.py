"""
 * 给你一个 2 行 n 列的二进制数组：
 * 1、矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
 * 2、第 0 行的元素之和为 upper。
 * 3、第 1 行的元素之和为 lower。
 * 4、第 i 列（从 0 开始编号）的元素之和为 col_sum[i]，col_sum 是一个长度为 n 的整数数组。
 * 你需要利用 upper，lower 和 col_sum 来重构这个矩阵，并以二维整数数组的形式返回它。
 * 如果有多个不同的答案，那么任意一个都可以通过本题。
 * 如果不存在符合要求的答案，就请返回一个空的二维数组。
 * 提示：
 * 1、1 <= col_sum.length <= 10^5
 * 2、0 <= upper, lower <= col_sum.length
 * 3、0 <= col_sum[i] <= 2
 * 链接：https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/
"""
from typing import List


class Solution:

    def reconstructMatrix(self, upper: int, lower: int, col_sum: List[int]) -> List[List[int]]:
        n = len(col_sum)
        arr1, arr2 = [0] * n, [0] * n
        s1 = set()
        for i in range(n):
            if col_sum[i] == 2:
                arr1[i] = 1
                arr2[i] = 1
                upper -= 1
                lower -= 1
            elif col_sum[i] == 1:
                s1.add(i)
        if upper < 0 or lower < 0: return []
        while s1:
            idx = s1.pop()
            if upper > 0:
                upper -= 1
                arr1[idx] = 1
            elif lower > 0:
                lower -= 1
                arr2[idx] = 1
            else:
                return []
        return [arr1, arr2] if upper == 0 and lower == 0 else []


if __name__ == '__main__':
    #
    print(Solution().reconstructMatrix(4, 7, [2, 1, 2, 2, 1, 1, 1]))
    # [[1,0,1],[0,1,0]]
    print(Solution().reconstructMatrix(2, 1, [1, 1, 1]))
    # []
    print(Solution().reconstructMatrix(2, 3, [2, 2, 1, 1]))
    # [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
    print(Solution().reconstructMatrix(5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))
