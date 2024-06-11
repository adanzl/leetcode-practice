"""
 * 给你一个任务数组 tasks ，其中 tasks[i] = [actual_i, minimum_i] ：
 * 1、actual_i 是完成第 i 个任务 需要耗费 的实际能量。
 * 2、minimum_i 是开始第 i 个任务前需要达到的最低能量。
 * 比方说，如果任务为 [10, 12] 且你当前的能量为 11 ，那么你不能开始这个任务。
 * 如果你当前的能量为 13 ，你可以完成这个任务，且完成它后剩余能量为 3 。
 * 你可以按照 任意顺序 完成任务。
 * 请你返回完成所有任务的 最少 初始能量。
 * 提示：
 * 1、1 <= tasks.length <= 10^5
 * 2、1 <= actual_i <= minimum_i <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/
"""

from typing import List

#
# @lc app=leetcode.cn id=1665 lang=python3
#
# [1665] 完成所有任务的最少初始能量
#


# @lc code=start
class Solution:

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        for a, m in sorted(tasks, key=lambda x: (x[1] - x[0])):
            ans += a
            ans = max(ans, m)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 8
    print(Solution().minimumEffort([[1, 2], [2, 4], [4, 8]]))
    # 32
    print(Solution().minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
    # 27
    print(Solution().minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
