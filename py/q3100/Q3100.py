"""
 * 给你两个整数 numBottles 和 numExchange 。
 * numBottles 代表你最初拥有的满水瓶数量。在一次操作中，你可以执行以下操作之一：
 * 1、喝掉任意数量的满水瓶，使它们变成空水瓶。
 * 2、用 numExchange 个空水瓶交换一个满水瓶。然后，将 numExchange 的值增加 1 。
 * 注意，你不能使用相同的 numExchange 值交换多批空水瓶。
 * 例如，如果 numBottles == 3 并且 numExchange == 1 ，则不能用 3 个空水瓶交换成 3 个满水瓶。
 * 返回你 最多 可以喝到多少瓶水。
 * 提示：
 * 1、1 <= numBottles <= 100 
 * 2、1 <= numExchange <= 100
 * 链接：https://leetcode.cn/problems/water-bottles-ii/
"""


class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        ans = numBottles
        while n >= numExchange:
            ans += 1
            n += 1 - numExchange
            numExchange += 1
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().maxBottlesDrunk(10, numExchange=3))
    # 26
    print(Solution().maxBottlesDrunk(20, 1))
    # 15
    print(Solution().maxBottlesDrunk(13, numExchange=6))
