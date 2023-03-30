"""
 * 你有一台电脑，它可以 同时 运行无数个任务。
 * 给你一个二维整数数组 tasks ，其中 tasks[i] = [start_i, end_i, duration_i] 表示第 i 个任务需要在 闭区间 时间段 
 * [start_i, end_i] 内运行 duration_i 个整数时间点（但不需要连续）。
 * 当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。
 * 请你返回完成所有任务的情况下，电脑最少需要运行多少秒。
 * 提示：
 * 1、1 <= tasks.length <= 2000
 * 2、tasks[i].length == 3
 * 3、1 <= start_i, end_i <= 2000
 * 4、1 <= duration_i <= end_i - start_i + 1
 * 链接：https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/
"""
from typing import List


class Solution:

    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        run = [False] * 2001
        for start, end, d in tasks:
            d -= sum(run[start:end + 1])  # 统计已经是运行中的时间点
            if d > 0:
                for i in range(end, start - 1, -1):  # 剩余的 d 填充区间后缀
                    if run[i]: continue
                    run[i] = True
                    d -= 1
                    if d == 0: break
        return sum(run)


if __name__ == '__main__':
    # 2
    print(Solution().findMinimumTime([[2, 3, 1], [4, 5, 1], [1, 5, 2]]))
    # 4
    print(Solution().findMinimumTime([[1, 3, 2], [2, 5, 3], [5, 6, 2]]))