"""
 * 给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。
 * 这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。
 * 请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 109 + 7 取余 后返回。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、1 <= k <= n-1
 * 链接：https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/
"""
from functools import cache
from math import comb


class Solution:

    def numberOfSets1(self, n: int, k: int) -> int:
        # 会超时
        MOD = 10**9 + 7

        @cache
        def f(n, k):
            if k == 1: return n * (n + 1) // 2 % MOD
            ret = 0
            for i in range(1, n - k + 2):
                ret += f(n - i, k - 1) * i % MOD  # 乘法原则
            return ret

        return f(n - 1, k) % MOD

    def numberOfSets(self, n: int, k: int) -> int:
        # 组合数 题意为n个点中选取k个线段，端点可重复，增加k-1个虚拟点（x_0-x_k-1），x_0被选中说明第0、1个线段有一个公共点，可能有k-1个
        # https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/solution/shuxuefa-by-oqelhurpka-zxdk/
        return comb(n + k - 1, 2 * k) % (10**9 + 7)

    def numberOfSets2(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        n -= 1
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        col = [0] * (k + 1)  # 前缀和优化，我也不知道为啥，看数猜出来的
        for i in range(1, n + 1):
            dp[i][1] = i * (i + 1) // 2
            col[1] += dp[i][1]
            for j in range(2, k + 1):  # split
                dp[i][j] = col[j - 1] + dp[i - 1][j] - dp[i][j - 1]
                col[j] += dp[i][j]
                # 未优化的状态转移，会超时
                # for l in range(1, i - j + 2):  # length
                #     dp[i][j] += l * dp[i - l][j - 1]

        return dp[-1][-1] % MOD


if __name__ == '__main__':
    # 88243036
    print(Solution().numberOfSets(751, 201))
    # 7
    print(Solution().numberOfSets(5, 3))
    # 796297179
    print(Solution().numberOfSets(30, 7))
    # 3
    print(Solution().numberOfSets(3, 1))
    # 5
    print(Solution().numberOfSets(4, 2))
    # 1
    print(Solution().numberOfSets(3, 2))
