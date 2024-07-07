"""
 * 超市正在促销，你可以用 numExchange 个空水瓶从超市兑换一瓶水。
 * 最开始，你一共购入了 numBottles 瓶水。
 * 如果喝掉了水瓶中的水，那么水瓶就会变成空的。
 * 给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。
 * 提示：
 * 1、1 <= numBottles <= 100
 * 2、2 <= numExchange <= 100
 * 链接：https://leetcode.cn/problems/water-bottles
"""

#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#


# @lc code=start
class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            a, r = divmod(numBottles, numExchange)
            ans += a
            numBottles = r + a
        return ans


# @lc code=end

if __name__ == '__main__':
    # 19
    print(Solution().numWaterBottles(15, numExchange=4))
    # 13
    print(Solution().numWaterBottles(9, numExchange=3))
    #
    # print(Solution().numWaterBottles())
