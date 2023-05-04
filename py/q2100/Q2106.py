"""
 * 在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。
 * 给你一个二维整数数组 fruits ，其中 fruits[i] = [position_i, amount_i] 表示共有 amount_i 个水果放置在 position_i 上。
 * fruits 已经按 position_i 升序排列 ，每个 position_i 互不相同 。
 * 另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。
 * 在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。
 * 你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。
 * 返回你可以摘到水果的 最大总数 。
 * 提示：
 * 1、1 <= fruits.length <= 10^5
 * 2、fruits[i].length == 2
 * 3、0 <= startPos, position_i <= 2 * 10^5
 * 4、对于任意 i > 0 ，position_i-1 < position_i 均成立（下标从 0 开始计数）
 * 5、1 <= amount_i <= 10^4
 * 6、0 <= k <= 2 * 10^5
 * 链接：https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps
"""
import bisect
from itertools import accumulate
from typing import List


class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], s: int, k: int) -> int:
        n = len(fruits)
        pre_sum = [[0, 0]] + list(accumulate(fruits, lambda x, y: [x[0] + y[0], x[1] + y[1]]))
        ans = 0
        for l in range(k + 1):
            if l <= k // 2:  # l-r
                r = k - l * 2  # [s-l*2, s+r]
                il = bisect.bisect_left(fruits, s - l, key=lambda x: x[0])
                ir = bisect.bisect_right(fruits, s + r, key=lambda x: x[0])  # [il, ir-1]
                ans = max(ans, pre_sum[min(ir, n)][1] - pre_sum[il][1])
            r = (k - l) // 2  # r-l
            if r >= 0:
                il = bisect.bisect_left(fruits, s - l, key=lambda x: x[0])
                ir = bisect.bisect_right(fruits, s + r, key=lambda x: x[0])
                ans = max(ans, pre_sum[min(ir, n)][1] - pre_sum[il][1])

        return ans


if __name__ == '__main__':
    # 71
    print(Solution().maxTotalFruits(
        [[0, 7], [7, 4], [9, 10], [12, 6], [14, 8], [16, 5], [17, 8], [19, 4], [20, 1], [21, 3], [24, 3], [25, 3], [26, 1], [28, 10], [30, 9], [31, 6], [32, 1], [37, 5], [40, 9]], s=21, k=30))
    # 0
    print(Solution().maxTotalFruits([[0, 3], [6, 4], [8, 5]], s=3, k=2))
    # 10000
    print(Solution().maxTotalFruits([[200000, 10000]], s=200000, k=200000))
    # 14
    print(Solution().maxTotalFruits([[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], s=5, k=4))
    # 9
    print(Solution().maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, k=4))
