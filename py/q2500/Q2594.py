"""
 * 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranks_i 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n^2 分钟内修好 n 辆车。
 * 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
 * 请你返回修理所有汽车 最少 需要多少时间。
 * 注意：所有机械工可以同时修理汽车。
 * 提示：
 * 1、1 <= ranks.length <= 10^5
 * 2、1 <= ranks[i] <= 100
 * 3、1 <= cars <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-time-to-repair-cars/
"""
import math
from typing import List


class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, 10**14
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            sm = 0
            for rank in ranks:
                sm += int(math.sqrt(mid // rank))
            if sm >= cars:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 576
    print(Solution().repairCars([1, 1, 3, 3], 74))
    # 16
    print(Solution().repairCars([5, 1, 8], cars=6))
    # 16
    print(Solution().repairCars([4, 2, 3, 1], cars=10))