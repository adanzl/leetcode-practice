"""
 * 提示：
 * 1、1 <= k <= events.length
 * 2、1 <= k * events.length <= 10^6
 * 3、1 <= startDay_i <= endDay_i <= 10^9
 * 4、1 <= value_i <= 10^6
 * 链接：https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/
"""
from bisect import bisect_right
from typing import List


class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]  # dp[i][j] 前i个任务，最多完成j个，最大得分
        for i, (s, e, v) in enumerate(events):
            idx = bisect_right(events, s - 1, key=lambda x: x[1])
            for j in range(k):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[idx][j] + v)
        return dp[-1][-1]


if __name__ == '__main__':
    # 10
    print(Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2))
    # 7
    print(Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2))
    # 9
    print(Solution().maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3))
