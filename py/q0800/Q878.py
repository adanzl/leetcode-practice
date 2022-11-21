"""
 * 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
 * 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。
 * 提示：
 * 1、1 <= n <= 10^9
 * 2、2 <= a, b <= 4 * 10^4
 * 链接：https://leetcode.cn/problems/nth-magical-number/
"""
from math import lcm


class Solution:

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ln = lcm(a, b)
        l, r = min(a, b), max(a, b) * n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if (mid // a + mid // b) - mid // ln >= n:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans % (10**9 + 7)


if __name__ == '__main__':
    # 6
    print(Solution().nthMagicalNumber(4, 2, 3))
    # 2
    print(Solution().nthMagicalNumber(1, 2, 3))
    #
    # print(Solution().nthMagicalNumber())