"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。
 * 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。
 * 如果以下条件满足，我们称这些塔是 美丽 的：
 * 1、1 <= heights[i] <= maxHeights[i]
 * 2、heights 是一个 山状 数组。
 * 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山状 数组：
 * 1、对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
 * 2、对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
 * 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。
 * 提示：
 * 1、1 <= n == maxHeights <= 10^3
 * 2、1 <= maxHeights[i] <= 10^9
 * 链接：https://leetcode.cn/problems/beautiful-towers-i/
"""
from typing import List


class Solution:

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        lh, rh = [0] * n, [0] * n
        for i in range(n):
            lh[i] = pre = maxHeights[i]
            for j in range(i + 1, n):
                pre = min(pre, maxHeights[j])
                lh[i] += pre
        ans = 0
        for i in range(n - 1, -1, -1):
            rh[i] = pre = maxHeights[i]
            for j in range(i - 1, -1, -1):
                pre = min(pre, maxHeights[j])
                rh[i] += pre
            ans = max(ans, lh[i] + rh[i] - maxHeights[i])
        return ans


if __name__ == '__main__':
    # 18
    print(Solution().maximumSumOfHeights([3, 2, 5, 5, 2, 3]))
    # 22
    print(Solution().maximumSumOfHeights([6, 5, 3, 9, 2, 7]))
    # 13
    print(Solution().maximumSumOfHeights([5, 3, 4, 1, 1]))
