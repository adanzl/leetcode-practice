"""
 * 给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。
 * 你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。
 * 返回使用这些硬币能制造的 第 k_th 小 金额。
 * 提示：
 * 1、1 <= coins.length <= 15
 * 2、1 <= coins[i] <= 25
 * 3、1 <= k <= 2 * 10^9
 * 4、coins 包含两两不同的整数
 * 链接：https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/
"""
from math import lcm
from typing import List


class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # 容斥原理 子集对结果的贡献 (−1)^(k−1) ⌊lcm/m⌋  k表示子集元素个数
        def check(m: int) -> bool:
            cnt = 0
            for i in range(1, 1 << len(coins)):  # 枚举所有非空子集
                lcm_res = 1  # 计算子集 LCM
                for j, x in enumerate(coins):
                    if i >> j & 1:
                        lcm_res = lcm(lcm_res, x)
                        if lcm_res > m:  # 太大了
                            break
                else:  # 中途没有 break
                    cnt += m // lcm_res if i.bit_count() % 2 else -(m // lcm_res)
            return cnt >= k

        l, r = 1, 10**12
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().findKthSmallest([3, 6, 9], k=3))
    # 88434
    print(Solution().findKthSmallest([20, 6, 15, 16, 22], 25727))
    # 4
    print(Solution().findKthSmallest([6, 1, 2, 4], 4))
    # 6
    print(Solution().findKthSmallest([3, 6, 10, 8, 1], 6))
    # 12
    print(Solution().findKthSmallest([5, 2], k=7))
