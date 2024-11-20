"""
 * 给你一个整数 n ，表示有 n 间零售商店。总共有 m 种产品，每种产品的数目用一个下标从 0 开始的整数数组 quantities 表示，
 * 其中 quantities[i] 表示第 i 种商品的数目。
 * 你需要将 所有商品 分配到零售商店，并遵守这些规则：
 * 1、一间商店 至多 只能有 一种商品 ，但一间商店拥有的商品数目可以为 任意 件。
 * 2、分配后，每间商店都会被分配一定数目的商品（可能为 0 件）。用 x 表示所有商店中分配商品数目的最大值，你希望 x 越小越好。
 *      也就是说，你想 最小化 分配给任意商店商品数目的 最大值 。
 * 请你返回最小的可能的 x 。
 * 提示：
 * m == quantities.length
 * 1 <= m <= n <= 10^5
 * 1 <= quantities[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store
"""

from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=2064 lang=python3
# @lcpr version=20003
#
# [2064] 分配给商店的最多商品的最小值
#


# @lc code=start
class Solution:

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def check(v):
            vv = 0
            for q in quantities:
                vv += (q + v - 1) // v
            return vv <= n

        lo, hi = 1, max(quantities) + 1
        ans = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid
            else:
                lo = mid + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().minimizedMaximum(1, quantities=[1]))
    # 100000
    print(Solution().minimizedMaximum(1, quantities=[100000]))
    # 3
    print(Solution().minimizedMaximum(6, quantities=[11, 6]))
    # 5
    print(Solution().minimizedMaximum(7, quantities=[15, 10, 10]))
