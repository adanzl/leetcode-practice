"""
 * 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
 * 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
 * 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
 * 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
 * 提示：
 * 1、1 <= n <= 100
 * 2、0 <= minProfit <= 100
 * 3、1 <= group.length <= 100
 * 4、1 <= group[i] <= 100
 * 5、profit.length == group.length
 * 6、0 <= profit[i] <= 100
 * 链接：https://leetcode.cn/problems/profitable-schemes/
"""

from typing import *


class Solution:

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        # 0-1 容量为n，前idx个任务，背包
        dp = [[1] + [0] * (minProfit) for _ in range(n + 1)]
        for g, p in zip(group, profit):  # task
            for c in range(n, g - 1, -1):  # capacity
                for i in range(minProfit, -1, -1):  # profit
                    u = max(i - p, 0)
                    dp[c][i] = (dp[c][i] + dp[c - g][u]) % MOD
        return sum([i for i in dp[n][minProfit:] if i > 0]) % MOD


if __name__ == '__main__':
    # 2
    print(Solution().profitableSchemes(5, 3, [2, 2], [2, 3]))
    # 7
    print(Solution().profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
