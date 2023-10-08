"""
 * 给你两个正整数 n 和 m 。
 * 现定义两个整数 num1 和 num2 ，如下所示：
 * 1、num1：范围 [1, n] 内所有 无法被 m 整除 的整数之和。
 * 2、num2：范围 [1, n] 内所有 能够被 m 整除 的整数之和。
 * 返回整数 num1 - num2 。
 * 提示：1 <= n, m <= 1000
 * 链接：https://leetcode.cn/problems/divisible-and-non-divisible-sums-difference/
"""


class Solution:

    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for num in range(1, n + 1):
            if num % m != 0:
                num1 += num
            else:
                num2 += num
        return num1 - num2


if __name__ == '__main__':
    # 19
    print(Solution().differenceOfSums(10, m=3))
    # 15
    print(Solution().differenceOfSums(5, m=6))
    # -15
    print(Solution().differenceOfSums(5, 1))
