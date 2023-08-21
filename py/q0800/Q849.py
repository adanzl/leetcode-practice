"""
 * 给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。
 * 至少有一个空座位，且至少有一人已经坐在座位上。
 * 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
 * 返回他到离他最近的人的最大距离。
 * 提示：
 * 1、2 <= seats.length <= 2 * 10^4
 * 2、seats[i] 为 0 或 1
 * 3、至少有一个 空座位
 * 4、至少有一个 座位上有人
 * 链接：https://leetcode.cn/problems/maximize-distance-to-closest-person/
"""
from typing import List


class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        lst = -1
        for i, v in enumerate(seats):
            if v == 1:
                if lst == -1:
                    ans = i
                else:
                    ans = max(ans, (i - lst) // 2)
                lst = i
        return max(ans, len(seats) - lst - 1)


if __name__ == '__main__':
    # 2
    print(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    # 3
    print(Solution().maxDistToClosest([1, 0, 0, 0]))
    # 1
    print(Solution().maxDistToClosest([0, 1]))
