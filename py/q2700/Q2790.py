"""
 * 给你一个下标从 0 开始、长度为 n 的数组 usageLimits 。
 * 你的任务是使用从 0 到 n - 1 的数字创建若干组，并确保每个数字 i 在 所有组 中使用的次数总共不超过 usageLimits[i] 次。此外，还必须满足以下条件：
 * 1、每个组必须由 不同 的数字组成，也就是说，单个组内不能存在重复的数字。
 * 2、每个组（除了第一个）的长度必须 严格大于 前一个组。
 * 在满足所有条件的情况下，以整数形式返回可以创建的最大组数。
 * 提示：
 * 1、1 <= usageLimits.length <= 10^5
 * 2、1 <= usageLimits[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-number-of-groups-with-increasing-length/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        fre = sorted([-u for u in usageLimits])
        ans = 0
        l, r = 1, len(usageLimits) + 1
        while l <= r:
            mid = (l + r) // 2
            fit = True
            fre_q = fre[:]
            for v in range(mid, 0, -1):
                change = False
                while fre_q and v:
                    f = heappop(fre_q)
                    if v < -f:
                        if change: heappush(fre_q, f + v)
                        v = 0
                    else:
                        v += f
                        change = True
                if v:
                    fit = False
                    break
            if fit:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().maxIncreasingGroups([1, 4, 4, 6, 2]))
    # 3
    print(Solution().maxIncreasingGroups([2, 2, 2]))
    # 2
    print(Solution().maxIncreasingGroups([1, 5]))
    # 2
    print(Solution().maxIncreasingGroups([2, 1, 2]))
    # 3
    print(Solution().maxIncreasingGroups([1, 2, 5]))
    # 1
    print(Solution().maxIncreasingGroups([1, 1]))
