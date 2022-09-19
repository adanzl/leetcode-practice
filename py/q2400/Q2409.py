"""
 * Alice 和 Bob 计划分别去罗马开会。
 * 给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），
 * 而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。
 * 请你返回 Alice和 Bob 同时在罗马的天数。
 * 你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。
 * 提示：
 * 1、所有日期的格式均为 "MM-DD" 。
 * 2、Alice 和 Bob 的到达日期都 早于或等于 他们的离开日期。
 * 3、题目测试用例所给出的日期均为 非闰年 的有效日期。
 * 链接：https://leetcode.cn/problems/count-days-spent-together/
"""

from itertools import accumulate


class Solution:

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pre_sum = [0] + list(accumulate(months))  # 前缀和
        start, end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        return max(0, pre_sum[int(end[:2]) - 1] + int(end[-2:]) - pre_sum[int(start[:2]) - 1] - int(start[-2:]) + 1)


if __name__ == '__main__':
    # 3
    print(Solution().countDaysTogether("08-15", "08-18", "08-16", "08-19"))
    # 0
    print(Solution().countDaysTogether("10-01", "10-31", "11-01", "12-31"))