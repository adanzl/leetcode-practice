"""
 * 你打算利用空闲时间来做兼职工作赚些零花钱。
 * 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
 * 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
 * 注意，时间上出现重叠的 2 份工作不能同时进行。
 * 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
 * 提示：
 * 1、1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
 * 2、1 <= startTime[i] < endTime[i] <= 10^9
 * 3、1 <= profit[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
"""
from bisect import bisect_right, insort
from typing import List


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: (x[1], x[0]))
        ans = 0
        d = []
        for i in range(n):
            s, e, p = arr[i]
            idx = bisect_right(d, s, key=lambda x: (x[0]))
            v = p if idx == 0 else (d[idx - 1][1] + p)
            if idx < len(d) and d[idx][0] == e:
                d[idx][1] = max(d[idx][1], v)
            else:
                ii = bisect_right(d, e, key=lambda x: (x[0]))
                if ii == 0 or d[ii - 1][1] <= v:
                    insort(d, [e, v])
            ans = max(ans, v)
        return ans

    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 直接按照结束时间排序，统计安排了i个任务之后的最大时间
        arr = sorted(zip(endTime, startTime, profit))
        dp = [0] * (len(arr) + 1)
        for i, (e, s, p) in enumerate(arr):
            idx = bisect_right(arr, s, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[idx] + p)
        return dp[-1]


if __name__ == '__main__':
    # 20
    print(Solution().jobScheduling([24, 24, 7, 2, 1, 13, 6, 14, 18, 24], [27, 27, 20, 7, 14, 22, 20, 24, 19, 27], [6, 1, 4, 2, 3, 6, 5, 6, 9, 8]))
    # 18
    print(Solution().jobScheduling([4, 2, 4, 8, 2], [5, 5, 5, 10, 8], [1, 2, 8, 10, 4]))
    # 150
    print(Solution().jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
    # 120
    print(Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    # 6
    print(Solution().jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
