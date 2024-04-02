"""
 * 如果一个整数能够被其各个数位上的数字之和整除，则称之为 哈沙德数（Harshad number）。给你一个整数 x 。
 * 如果 x 是 哈沙德数 ，则返回 x 各个数位上的数字之和，否则，返回 -1 。
 * 提示：1 <= x <= 100
 * 链接：https://leetcode.cn/problems/harshad-number/
"""


class Solution:

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm, num = 0, x
        while num:
            sm += num % 10
            num //= 10
        return sm if x % sm == 0 else -1


if __name__ == '__main__':
    # 9
    print(Solution().sumOfTheDigitsOfHarshadNumber(18))
    # -1
    print(Solution().sumOfTheDigitsOfHarshadNumber(23))
