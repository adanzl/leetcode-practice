"""
 * 你有 n 颗处理器，每颗处理器都有 4 个核心。现有 n * 4 个待执行任务，每个核心只执行 一个 任务。
 * 给你一个下标从 0 开始的整数数组 processorTime ，表示每颗处理器最早空闲时间。
 * 另给你一个下标从 0 开始的整数数组 tasks ，表示执行每个任务所需的时间。返回所有任务都执行完毕需要的 最小时间 。
 * 注意：每个核心独立执行任务。
 * 提示：
 * 1、1 <= n == processorTime.length <= 25000
 * 2、1 <= tasks.length <= 10^5
 * 3、0 <= processorTime[i] <= 10^9
 * 4、1 <= tasks[i] <= 10^9
 * 5、tasks.length == 4 * n
 * 链接：https://leetcode.cn/problems/minimum-processing-time/
"""
from typing import List


class Solution:

    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        return max([t1 + t2 for t1, t2 in zip(sorted(tasks), sorted([t for _ in range(4) for t in processorTime], reverse=True))])


if __name__ == '__main__':
    # 16
    print(Solution().minProcessingTime([8, 10], tasks=[2, 2, 3, 1, 8, 7, 4, 5]))
    # 23
    print(Solution().minProcessingTime([10, 20], tasks=[2, 3, 1, 2, 5, 8, 4, 3]))
