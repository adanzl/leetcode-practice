"""
 * 给你两个长度相等的整数数组，返回下面表达式的最大值：
 * |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
 * 其中下标 i，j 满足 0 <= i, j < arr1.length。
 * 提示：
 * 1、2 <= arr1.length == arr2.length <= 4*10^4
 * 2、-10^6 <= arr1[i], arr2[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-of-absolute-value-expression/
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

#
# @lc app=leetcode.cn id=1131 lang=python3
# @lcpr version=30101
#
# [1131] 绝对值表达式的最大值
#


# @lc code=start
class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # 数学解法
        A, B, C, D = [], [], [], []
        for i, (x, y) in enumerate(zip(arr1, arr2)):
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)


# @lc code=end

#
# @lcpr case=start
# [1,2,3,4]\n[-1,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,-2,-5,0,10]\n[0,-2,-1,-7,-4]\n
# @lcpr case=end

#
if __name__ == '__main__':
    # 13
    print(Solution().maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6]))
    # 20
    print(Solution().maxAbsValExpr([1, -2, -5, 0, 10], [0, -2, -1, -7, -4]))
    #
    # print(Solution().maxAbsValExpr())
