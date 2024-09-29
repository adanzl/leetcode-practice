"""
 * 给你一个字符串 date，它的格式为 yyyy-mm-dd，表示一个公历日期。
 * date 可以重写为二进制表示，只需要将年、月、日分别转换为对应的二进制表示（不带前导零）并遵循 year-month-day 的格式。
 * 返回 date 的 二进制 表示。
 * 提示：
 * 1、date.length == 10
 * 2、date[4] == date[7] == '-'，其余的 date[i] 都是数字。
 * 3、输入保证 date 代表一个有效的公历日期，日期范围从 1900 年 1 月 1 日到 2100 年 12 月 31 日（包括这两天）。
 * 链接：https://leetcode.cn/problems/convert-date-to-binary/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def convertDateToBinary(self, date: str) -> str:
        ans = []
        for s in date.split('-'):
            ans.append(bin(int(s))[2:])
        return '-'.join(ans)


if __name__ == '__main__':
    # "100000100000-10-11101"
    print(Solution().convertDateToBinary("2080-02-29"))
    # "11101101100-1-1"
    print(Solution().convertDateToBinary("1900-01-01"))
