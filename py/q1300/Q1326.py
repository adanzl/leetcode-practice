"""
 * 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
 * 花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。
 * 给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。
 * 请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、ranges.length == n + 1
 * 3、0 <= ranges[i] <= 100
 * 链接：https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/
"""
from typing import List


class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        p_min = lambda a, b: a if a < b else b
        dp = [-1] * (n + 1)  # 地块
        dp[0] = 0
        for i, ra in enumerate(ranges):  # 龙头
            l, r = max(0, i - ra), p_min(n, i + ra)
            for j in range(l, i):  # 龙头
                if dp[j + 1] == -1: dp[j + 1] = dp[l] + 1
                else: dp[j + 1] = p_min(dp[j + 1], dp[l] + 1)
            for j in range(i + 1, r + 1):  # 龙头
                if dp[j] == -1: dp[j] = dp[l] + 1
                else: dp[j] = p_min(dp[j], dp[l] + 1)
        if min(dp) == -1: return -1
        return max(dp)


if __name__ == '__main__':
    # -1
    print(Solution().minTaps(3, [0, 0, 0, 0]))
    # 2
    print(Solution().minTaps(8, [4, 0, 0, 0, 0, 0, 0, 0, 4]))
    # 1
    print(Solution().minTaps(5, [3, 4, 1, 1, 0, 0]))
