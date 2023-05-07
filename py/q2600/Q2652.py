"""
 * 给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。
 * 返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。
 * 提示：1 <= n <= 10^3
 * 链接：https://leetcode.cn/problems/sum-multiples/
"""


class Solution:

    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                ans += num
        return ans


if __name__ == '__main__':
    # 21
    print(Solution().sumOfMultiples(7))
    # 40
    print(Solution().sumOfMultiples(10))
    # 30
    print(Solution().sumOfMultiples(9))