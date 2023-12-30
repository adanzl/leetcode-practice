"""
 * 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
 * 输入为三个整数：day、month 和 year，分别表示日、月、年。
 * 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
 * 提示：给出的日期一定是在 1971 到 2100 年之间的有效日期。
 * 链接：https://leetcode.cn/problems/day-of-the-week/
"""
from datetime import datetime


class Solution:

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday_num = datetime(year, month, day, 0, 0, 0).weekday()
        weekday_mapping = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday_mapping[weekday_num]


if __name__ == '__main__':
    # "Saturday"
    print(Solution().dayOfTheWeek(31, month=8, year=2019))
    # "Sunday"
    print(Solution().dayOfTheWeek(18, month=7, year=1999))
    # "Sunday"
    print(Solution().dayOfTheWeek(15, month=8, year=1993))
