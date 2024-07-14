"""
 * 有一个 m x n 大小的矩形蛋糕，需要切成 1 x 1 的小块。
 * 给你整数 m ，n 和两个数组：
 * 1、horizontalCut 的大小为 m - 1 ，其中 horizontalCut[i] 表示沿着水平线 i 切蛋糕的开销。
 * 2、verticalCut 的大小为 n - 1 ，其中 verticalCut[j] 表示沿着垂直线 j 切蛋糕的开销。
 * 一次操作中，你可以选择任意不是 1 x 1 大小的矩形蛋糕并执行以下操作之一：
 * 1、沿着水平线 i 切开蛋糕，开销为 horizontalCut[i] 。
 * 2、沿着垂直线 j 切开蛋糕，开销为 verticalCut[j] 。
 * 每次操作后，这块蛋糕都被切成两个独立的小蛋糕。
 * 每次操作的开销都为最开始对应切割线的开销，并且不会改变。
 * 请你返回将蛋糕全部切成 1 x 1 的蛋糕块的 最小 总开销。
 * 提示：
 * 1、1 <= m, n <= 10^5
 * 2、horizontalCut.length == m - 1
 * 3、verticalCut.length == n - 1
 * 4、1 <= horizontalCut[i], verticalCut[i] <= 10^3
 * 链接：https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/
"""
from typing import List


class Solution:

    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        h_hor, h_ver = sorted(horizontalCut, reverse=True), sorted(verticalCut, reverse=True)
        ans, i_m, i_n = 0, 0, 0

        while i_m < m - 1 and i_n < n - 1:
            h_val, v_val = h_hor[i_m], h_ver[i_n]
            if v_val > h_val:  # choose ver
                i_n += 1
                ans += v_val * (i_m + 1)
            else:
                i_m += 1
                ans += h_val * (i_n + 1)
        if i_m < m - 1:  # hor
            ans += (i_n + 1) * sum(h_hor[i_m:])
        if i_n < n - 1:  # ver
            ans += (i_m + 1) * sum(h_ver[i_n:])

        return ans


if __name__ == '__main__':
    # 28
    print(Solution().minimumCost(6, 3, [3, 3, 2, 2, 1], [2, 1]))
    # 15
    print(Solution().minimumCost(2, n=2, horizontalCut=[7], verticalCut=[4]))
    # 13
    print(Solution().minimumCost(3, n=2, horizontalCut=[1, 3], verticalCut=[5]))
