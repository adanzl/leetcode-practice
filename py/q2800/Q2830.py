"""
 * 给你一个整数 n 表示数轴上的房屋数量，编号从 0 到 n - 1 。
 * 另给你一个二维整数数组 offers ，其中 offers[i] = [start_i, end_i, gold_i] 表示第 i 个买家想要以 gold_i 枚金币的价格购买从 start_i 到 end_i 的所有房屋。
 * 作为一名销售，你需要有策略地选择并销售房屋使自己的收入最大化。
 * 返回你可以赚取的金币的最大数目。
 * 注意 同一所房屋不能卖给不同的买家，并且允许保留一些房屋不进行出售。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= offers.length <= 10^5
 * 3、offers[i].length == 3
 * 4、0 <= start_i <= end_i <= n - 1
 * 5、1 <= gold_i <= 10^3
 * 链接：https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/
"""
import bisect
from typing import List


class Solution:

    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        ln = len(offers)
        dp = [0] * (ln + 1)
        for i, (s, e, g) in enumerate(offers):
            idx = bisect.bisect_left(offers, s, key=lambda x: x[1], hi=i)
            if idx == i:
                dp[i + 1] = g + dp[i]
            else:
                dp[i + 1] = max(dp[i], dp[idx] + g)
        return dp[-1]


if __name__ == '__main__':
    # 10
    print(Solution().maximizeTheProfit(5, offers=[[0, 0, 1], [0, 2, 10], [1, 3, 2]]))
    # 3
    print(Solution().maximizeTheProfit(5, offers=[[0, 0, 1], [0, 2, 2], [1, 3, 2]]))