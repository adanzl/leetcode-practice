"""
 * 这里有 n 门不同的在线课程，按从 1 到 n 编号。
 * 给你一个数组 courses ，其中 courses[i] = [duration_i, lastDay_i] 表示第 i 门课将会 持续 上 duration_i 天课，
 * 并且必须在不晚于 lastDay_i 的时候完成。
 * 你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
 * 返回你最多可以修读的课程数目。
 * 提示:
 * 1、1 <= courses.length <= 10^4
 * 2、1 <= duration_i, lastDay_i <= 10^4
 * 链接：https://leetcode.cn/problems/course-schedule-iii
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#

# @lc code=start


class Solution:

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        q = []
        total = 0
        for dur, last in courses:
            if total + dur <= last:
                total += dur
                heappush(q, -dur)
            elif q and -q[0] > dur:
                total -= -q[0] - dur
                heappop(q)
                heappush(q, -dur)
        return len(q)


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().scheduleCourse([[1, 2], [2, 3]]))
    # 4
    print(Solution().scheduleCourse([[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 8], [6, 11], [3, 13], [6, 16]]))
    # 3
    print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
    # 1
    print(Solution().scheduleCourse([[1, 2]]))
    # 0
    print(Solution().scheduleCourse([[3, 2], [4, 3]]))
