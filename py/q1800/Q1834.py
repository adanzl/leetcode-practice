"""
 * 给你一个二维数组 tasks ，用于表示 n 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTime_i, processingTime_i] 
 * 意味着第 i 项任务将会于 enqueueTime_i 时进入任务队列，需要 processingTime_i 的时长完成执行。
 * 现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：
 * 1、如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
 * 2、如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
 * 3、一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
 * 4、CPU 可以在完成一项任务后，立即开始执行一项新任务。
 * 返回 CPU 处理任务的顺序。
 * 提示：
 * 1、tasks.length == n
 * 2、1 <= n <= 10^5
 * 3、1 <= enqueueTime_i, processingTime_i <= 10^9
 * 链接：https://leetcode.cn/problems/single-threaded-cpu/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        h = []  # p-i
        arr = sorted([[e, p, i] for i, (e, p) in enumerate(tasks)])
        time = arr[0][0]
        idx, n = 0, len(tasks)
        while idx < n or h:
            while idx < n and arr[idx][0] <= time:
                heappush(h, [arr[idx][1], arr[idx][2]])
                idx += 1
            if not h:
                heappush(h, [arr[idx][1], arr[idx][2]])
                time = arr[idx][0]
                idx += 1
            p, i = heappop(h)
            time += p
            ans.append(i)
        return ans


if __name__ == '__main__':
    # [0,2,3,1]
    print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
    # [4,3,2,0,1,5]
    print(Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2], [100, 1]]))
