"""
 * 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
 * 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
 * 找出把所有石头合并成一堆的 最低 成本。如果不可能，返回 -1 
 * 提示：
 * 1、1 <= stones.length <= 30
 * 2、2 <= K <= 30
 * 3、1 <= stones[i] <= 100
 * 链接：https://leetcode.cn/problems/minimum-cost-to-merge-stones/
"""
from typing import List


class Solution:

    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n % (k - 1) != 1 and k != 2: return -1
        inf = 0x3c3c3c3c
        # dp[i][j] 完全合并最小成本 i < j, l = (j-i+1-1)%(k-1)+1
        dp = [[[inf] * k for _ in range(n)] for __ in range(n)]  # from-to-cnt
        for i in range(n - 1, -1, -1):
            dp[i][i][1] = 0
            for j in range(i, n):
                for m in range(i, j):  # slice [i-m], [m+1, j]
                    l1, l2 = (m - i) % (k - 1) + 1, (j - m - 1) % (k - 1) + 1
                    sm = l1 + l2
                    # cost dp[i][j] = sum(stones[i:j + 1])
                    # dp[i][j] = dp[i][m] + dp[m+1][j] + cost
                    if sm >= k:
                        dp[i][j][sm - k + 1] = min(dp[i][j][sm - k + 1], dp[i][m][l1] + dp[m + 1][j][l2] + sum(stones[i:j + 1]))
                    else:
                        dp[i][j][sm] = min(dp[i][j][sm], dp[i][m][l1] + dp[m + 1][j][l2])
        return dp[0][-1][1]


if __name__ == '__main__':
    # 25
    print(Solution().mergeStones([3, 5, 1, 2, 6], 3))
    # 20
    print(Solution().mergeStones([3, 2, 4, 1], 2))
    # -1
    print(Solution().mergeStones([3, 2, 4, 1], 3))
