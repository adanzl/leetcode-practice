"""
 * 给你一个 n x n 的整数方阵 matrix 。你可以执行以下操作 任意次 ：
 * 选择 matrix 中 相邻 两个元素，并将它们都 乘以 -1 。
 * 如果两个元素有 公共边 ，那么它们就是 相邻 的。
 * 你的目的是 最大化 方阵元素的和。请你在执行以上操作之后，返回方阵的 最大 和。
 * 提示：
 * 1、n == matrix.length == matrix[i].length
 * 2、2 <= n <= 250
 * 3、-10^5 <= matrix[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-matrix-sum/
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, \
    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        sm_neg = 0
        mx_neg, mn_pos = -INF, INF
        i_z, i_p, i_n = 0, 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0:
                    ans += matrix[i][j]
                    mn_pos = min(mn_pos, matrix[i][j])
                    i_p += 1
                elif matrix[i][j] == 0:
                    i_z += 1
                else:
                    mx_neg = max(mx_neg, matrix[i][j])
                    sm_neg += matrix[i][j]
                    i_n += 1
        if i_z or i_n & 1 == 0:
            ans += -sm_neg
        else:
            ans += -sm_neg + max(mx_neg, -mn_pos) * 2
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maxMatrixSum([[1, -1], [-1, 1]]))
    # 16
    print(Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
