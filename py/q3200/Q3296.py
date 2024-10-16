"""
 * 给你一个整数 mountainHeight 表示山的高度。
 * 同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。
 * 工人们需要 同时 进行工作以 降低 山的高度。对于工人 i :
 * 山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 秒。例如：
 *      山的高度降低 1，需要 workerTimes[i] 秒。
 *      山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。
 * 返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。
 * 提示：
 * 1、1 <= mountainHeight <= 10^5
 * 2、1 <= workerTimes.length <= 10^4
 * 3、1 <= workerTimes[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero
"""
import math
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def check(v):
            ret = 0
            for t in workerTimes:
                ret += math.floor((math.sqrt(1 + 8* v / t) - 1) /2)
            return ret >= mountainHeight
        lo, hi = 0, INF
        ans = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
                ans = mid
            else:
                lo = mid + 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minNumberOfSeconds(4, workerTimes=[2, 1, 1]))
    # 12
    print(Solution().minNumberOfSeconds(10, workerTimes=[3, 2, 2, 4]))
    # 15
    print(Solution().minNumberOfSeconds(5, workerTimes=[1]))
