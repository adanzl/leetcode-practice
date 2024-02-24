"""
 * 给你一个整数 k 和一个整数 x 。
 * 令 s 为整数 num 的下标从 1 开始的二进制表示。
 * 我们说一个整数 num 的 价值 是满足 i % x == 0 且 s[i] 是 设置位 的 i 的数目。
 * 请你返回 最大 整数 num ，满足从 1 到 num 的所有整数的 价值 和小于等于 k 。
 * 注意：
 * 1、一个整数二进制表示下 设置位 是值为 1 的数位。
 * 2、一个整数的二进制表示下标从右到左编号，比方说如果 s == 11100 ，那么 s[4] == 1 且 s[2] == 0 。
 * 提示：
 * 1、1 <= k <= 10^15
 * 2、1 <= x <= 8
 * 链接：https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
"""


class Solution:

    def findMaximumNumber(self, k: int, x: int) -> int:
        l, r = 1, 10**15
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            ii = x
            sm = 0
            while 1 << (ii - 1) <= mid:
                a, rr = divmod(mid, 1 << ii)
                vv = 1 << (ii - 1)
                sm += a * vv
                rr += 1
                if rr > vv:
                    sm += rr - vv
                ii += x
            if sm <= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # 50
    print(Solution().findMaximumNumber(19, 6))
    # 9
    print(Solution().findMaximumNumber(7, x=2))
    # 6
    print(Solution().findMaximumNumber(9, x=1))
