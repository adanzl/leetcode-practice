"""
 * 给你两个字符串数组 event1 和 event2 ，表示发生在同一天的两个闭区间时间段事件，其中：
 * 1、event1 = [startTime1, endTime1] 且
 * 2、event2 = [startTime2, endTime2]
 * 事件的时间为有效的 24 小时制且按 HH:MM 格式给出。
 * 当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 冲突 。
 * 如果两个事件之间存在冲突，返回 true ；否则，返回 false 。
 * 提示：
 * 1、event1.length == event2.length == 2.
 * 2、event1[i].length == event2[i].length == 5
 * 3、startTime1 <= endTime1
 * 4、startTime2 <= endTime2
 * 5、所有事件的时间都按照 HH:MM 格式给出
 * 链接：https://leetcode.cn/problems/determine-if-two-events-have-conflict/
"""
from typing import List


class Solution:

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event2[0] <= event1[0] <= event2[1] or event2[0] <= event1[1] <= event2[1] or event1[0] <= event2[0] <= event1[1] or event1[0] <= event2[1] <= event1[1]


if __name__ == '__main__':
    # true
    print(Solution().haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))
    # true
    print(Solution().haveConflict(["01:00", "02:00"], ["01:20", "03:00"]))
    # false
    print(Solution().haveConflict(["10:00", "11:00"], ["14:00", "15:00"]))
