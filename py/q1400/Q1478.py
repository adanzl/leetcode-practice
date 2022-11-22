"""
 * 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。
 * 请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。
 * 答案保证在 32 位有符号整数范围以内。
 * 提示：
 * 1、n == houses.length
 * 2、1 <= n <= 100
 * 3、1 <= houses[i] <= 10^4
 * 4、1 <= k <= n
 * 5、数组 houses 中的整数互不相同。
 * 链接：https://leetcode.cn/problems/allocate-mailboxes/
"""
from typing import List


class Solution:

    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        inf = 0x3c3c3c3c
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):  # house
            for j in range(k):  # post
                for l in range(i, -1, -1):
                    # 最后一个post覆盖的房子数
                    cost, lp, rp = 0, l, i
                    while lp <= rp:
                        cost += houses[rp] - houses[lp]
                        lp += 1
                        rp -= 1
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[l][j] + cost)
        return dp[-1][-1]


if __name__ == '__main__':
    # 8
    print(Solution().minDistance([7, 4, 6, 1], k=1))
    # 5
    print(Solution().minDistance([1, 4, 8, 10, 20], k=3))
    # 9
    print(Solution().minDistance([2, 3, 5, 12, 18], k=2))
    # 0
    print(Solution().minDistance([3, 6, 14, 10], k=4))
