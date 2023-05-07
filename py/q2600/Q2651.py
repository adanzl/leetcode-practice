"""
 * 给你一个正整数 arrivalTime 表示列车正点到站的时间（单位：小时），另给你一个正整数 delayedTime 表示列车延误的小时数。
 * 返回列车实际到站的时间。
 * 注意，该问题中的时间采用 24 小时制。
 * 提示：
 * 1、1 <= arrivalTime < 24
 * 2、1 <= delayedTime <= 24
 * 链接：https://leetcode.cn/problems/calculate-delayed-arrival-time/
"""


class Solution:

    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == '__main__':
    # 20
    print(Solution().findDelayedArrivalTime(15, delayedTime=5))
    # 0
    print(Solution().findDelayedArrivalTime(13, delayedTime=11))
