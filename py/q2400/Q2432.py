"""
 * 共有 n 位员工，每位员工都有一个从 0 到 n - 1 的唯一 id 。
 * 给你一个二维整数数组 logs ，其中 logs[i] = [id_i, leaveTime_i] ：
 * 1、id_i 是处理第 i 个任务的员工的 id ，且
 * 2、leaveTime_i 是员工完成第 i 个任务的时刻。所有 leaveTime_i 的值都是 唯一 的。
 * 注意，第 i 个任务在第 (i - 1) 个任务结束后立即开始，且第 0 个任务从时刻 0 开始。
 * 返回处理用时最长的那个任务的员工的 id 。如果存在两个或多个员工同时满足，则返回几人中 最小 的 id 。
 * 提示：
 * 1、2 <= n <= 500
 * 2、1 <= logs.length <= 500
 * 3、logs[i].length == 2
 * 4、0 <= id_i <= n - 1
 * 5、1 <= leaveTime_i <= 500
 * 6、id_i != id_i + 1
 * 7、leaveTime_i 按严格递增顺序排列
 * 链接：https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task/
"""
from typing import List


class Solution:

    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time = dict()  # time-id
        time[logs[0][1]] = logs[0][0]
        for i in range(1, len(logs)):
            t = logs[i][1] - logs[i - 1][1]
            if t not in time:
                time[t] = logs[i][0]
            else:
                time[t] = min(logs[i][0], time[t])
        return sorted([[k, v] for k, v in time.items()], key=lambda x: x[0], reverse=True)[0][1]


if __name__ == '__main__':
    # 12
    print(Solution().hardestWorker(70, [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]))
    # 1
    print(Solution().hardestWorker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]))
