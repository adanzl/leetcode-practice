"""
 * 链接：https://leetcode.cn/problems/count-ways-to-make-array-with-product/
"""
from functools import cache
from typing import List
# import sys

# sys.setrecursionlimit(5 * 10**5)


class Solution:

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        # 约数 预处理
        N = 105
        divisors = [[] for _ in range(N)]
        for i in range(2, N):
            for j in range(i, N, i):
                divisors[j].append(i)
        dp = [[0] * N for _ in range(N)]  # dp[i][j] i个数 乘积是j
        for i in range(N):
            dp[1][i] = 1
        for i in range(2, N):  # i th
            for j in range(1, N):  # end with j
                for l in range(1, N // j):
                    dp[i][l * j] += dp[i - 1][l]
        # @cache
        # def f(n, k):
        #     if k == 1 or n == 1: return 1
        #     ret = f(n - 1, k)
        #     for d in divisors[k]:
        #         ret += f(n - 1, k // d)
        #     return ret

        ans = []
        for ni, ki in queries:
            # ans.append(f(ni, ki) % MOD)
            ans.append(dp[ni][ki] % MOD)
        return ans


if __name__ == '__main__':
    # [4,1,50734910]
    print(Solution().waysToFillArray([[2, 6], [5, 1], [73, 660]]))
    # [1,2,3,10,5]
    print(Solution().waysToFillArray([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
    #
    # print(Solution().waysToFillArray([[2, 6], [5, 1], [10000, 10000]]))