"""
 * 给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。
 * 每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。
 * 给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。
 * 提示：
 * 1、1 <= time.length <= 10^5
 * 2、1 <= time[i], totalTrips <= 10^7
 * 链接：https://leetcode.cn/problems/minimum-time-to-complete-trips/
"""
from typing import List


class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, 10**15
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            sm = 0
            for t in time:
                sm += mid // t
            if sm >= totalTrips:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 100000000000000
    print(Solution().minimumTime([10000000], totalTrips=10000000))
    # 3
    print(Solution().minimumTime([1, 2, 3], totalTrips=5))
    # 2
    print(Solution().minimumTime([2], totalTrips=1))
