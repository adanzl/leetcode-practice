"""
 * 给你 n 个项目，编号从 0 到 n - 1 。同时给你一个整数数组 milestones ，其中每个 milestones[i] 表示第 i 个项目中的阶段任务数量。
 * 你可以按下面两个规则参与项目中的工作：
 * 1、每周，你将会完成 某一个 项目中的 恰好一个 阶段任务。你每周都 必须 工作。
 * 2、在 连续的 两周中，你 不能 参与并完成同一个项目中的两个阶段任务。
 * 一旦所有项目中的全部阶段任务都完成，或者仅剩余一个阶段任务都会导致你违反上面的规则，那么你将 停止工作 。
 * 注意，由于这些条件的限制，你可能无法完成所有阶段任务。
 * 返回在不违反上面规则的情况下你 最多 能工作多少周。
 * 提示：
 * 1、n == milestones.length
 * 2、1 <= n <= 10^5
 * 3、1 <= milestones[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=1953 lang=python3
#
# [1953] 你可以工作的最大周数
#


# @lc code=start
class Solution:

    def numberOfWeeks(self, milestones: List[int]):
        # 耗时最长工作所需周数
        longest = max(milestones)
        # 其余工作共计所需周数
        rest = sum(milestones) - longest
        if longest > rest + 1:
            # 此时无法完成所耗时最长的工作
            return rest * 2 + 1
        # 此时可以完成所有工作
        return longest + rest


# @lc code=end

if __name__ == '__main__':
    # 40
    print(Solution().numberOfWeeks([5, 7, 5, 7, 9, 7]))
    # 29
    print(Solution().numberOfWeeks([9, 3, 6, 8, 2, 1]))
    # 6
    print(Solution().numberOfWeeks([1, 2, 3]))
    # 7
    print(Solution().numberOfWeeks([5, 2, 1]))
