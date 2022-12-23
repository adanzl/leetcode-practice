"""
 * 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
 * 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
 * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
 * 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 提示：
 * 1、1 <= prices.length <= 5000
 * 2、0 <= prices[i] <= 1000
 * 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/
"""
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = [-0x3c3c3c3c, -0x3c3c3c3c, 0, -0x3c3c3c3c]  # buy-sell-cool-hold
        for c in prices:
            dp = [
                dp[2] - c,
                max(dp[0] + c, dp[3] + c),
                max(dp[2], dp[1]),
                max(dp[0], dp[3]),
            ]
        return max(dp)


if __name__ == '__main__':
    # 3
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
    # 0
    print(Solution().maxProfit([1]))