"""
 * 你在一个水果超市里，货架上摆满了玲琅满目的奇珍异果。
 * 给你一个下标从 1 开始的数组 prices ，其中 prices[i] 表示你购买第 i 个水果需要花费的金币数目。
 * 水果超市有如下促销活动：
 * 如果你花费 price[i] 购买了水果 i ，那么接下来的 i 个水果你都可以免费获得。
 * 注意 ，即使你 可以 免费获得水果 j ，你仍然可以花费 prices[j] 个金币去购买它以便能免费获得接下来的 j 个水果。
 * 请你返回获得所有水果所需要的 最少 金币数。
 * 提示：
 * 1、1 <= prices.length <= 1000
 * 2、1 <= prices[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-number-of-coins-for-fruits
"""
from typing import List


class Solution:

    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [10**30] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = min(dp[i - 1] + prices[i - 1], dp[i])
            for j in range(i + 1, min(n + 1, i + i + 1)):
                dp[j] = min(dp[j], dp[i - 1] + prices[i - 1])
        return dp[-1]


if __name__ == '__main__':
    # 2
    print(Solution().minimumCoins([1, 10, 1, 1]))
    # 4
    print(Solution().minimumCoins([3, 1, 2]))
