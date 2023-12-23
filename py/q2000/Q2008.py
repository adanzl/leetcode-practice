"""
 * 你驾驶出租车行驶在一条有 n 个地点的路上。这 n 个地点从近到远编号为 1 到 n ，你想要从 1 开到 n ，通过接乘客订单盈利。
 * 你只能沿着编号递增的方向前进，不能改变方向。
 * 乘客信息用一个下标从 0 开始的二维数组 rides 表示，
 * 其中 rides[i] = [start_i, end_i, tip_i] 表示第 i 位乘客需要从地点 start_i 前往 end_i ，愿意支付 tip_i 元的小费。
 * 每一位 你选择接单的乘客 i ，你可以 盈利 end_i - start_i + tip_i 元。你同时 最多 只能接一个订单。
 * 给你 n 和 rides ，请你返回在最优接单方案下，你能盈利 最多 多少元。
 * 注意：你可以在一个地点放下一位乘客，并在同一个地点接上另一位乘客。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= rides.length <= 3 * 10^4
 * 3、rides[i].length == 3
 * 4、1 <= start_i < end_i <= n
 * 5、1 <= tipi <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-earnings-from-taxi
"""

from typing import List

#
# @lc app=leetcode.cn id=2008 lang=python3
#
# [2008] 出租车的最大盈利
#


# @lc code=start
class Solution:

    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort()
        ii = 0
        for i in range(n):
            while ii < len(rides) and rides[ii][0] == i:
                s, e, t = rides[ii]
                dp[e] = max(dp[e], dp[s] + (e - s + t))
                ii += 1
            dp[i + 1] = max(dp[i + 1], dp[i])
        return dp[-1]


# @lc code=end

if __name__ == '__main__':
    # 20
    print(Solution().maxTaxiEarnings(20,
                                     rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]))
    # 7
    print(Solution().maxTaxiEarnings(5, rides=[[2, 5, 4], [1, 5, 1]]))
    #
    # print(Solution().maxTaxiEarnings())
