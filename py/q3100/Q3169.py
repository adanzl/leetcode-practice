"""
 * 给你一个正整数 days，表示员工可工作的总天数（从第 1 天开始）。
 * 另给你一个二维数组 meetings，长度为 n，其中 meetings[i] = [start_i, end_i] 表示第 i 次会议的开始和结束天数（包含首尾）。
 * 返回员工可工作且没有安排会议的天数。
 * 注意：会议时间可能会有重叠。
 * 提示：
 * 1、1 <= days <= 10^9
 * 2、1 <= meetings.length <= 10^5
 * 3、meetings[i].length == 2
 * 4、1 <= meetings[i][0] <= meetings[i][1] <= days
 * 链接：https://leetcode.cn/problems/count-days-without-meetings/
"""
from typing import List


class Solution:

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = 0
        flag = 0
        for s, e in meetings:
            ans += max(0, s - flag - 1)
            flag = max(flag, e)
        return ans + max(0, days - flag)


if __name__ == '__main__':
    # 1
    print(Solution().countDays(8, [[3, 4], [4, 8], [2, 5], [3, 8]]))
    # 1
    print(Solution().countDays(5, meetings=[[2, 4], [1, 3]]))
    # 2
    print(Solution().countDays(10, meetings=[[5, 7], [1, 3], [9, 10]]))
    # 0
    print(Solution().countDays(6, meetings=[[1, 6]]))
