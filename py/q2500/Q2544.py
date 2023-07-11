"""
 * 给你一个正整数 n 。n 中的每一位数字都会按下述规则分配一个符号：
 * 1、最高有效位 上的数字分配到 正 号。
 * 2、剩余每位上数字的符号都与其相邻数字相反。
 * 返回所有数字及其对应符号的和。
 * 提示：1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/alternating-digit-sum/
"""


class Solution:

    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        f = 1
        for c in str(n):
            ans += int(c) * f
            f *= -1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().alternateDigitSum(521))
    # 1
    print(Solution().alternateDigitSum(111))
    # 0
    print(Solution().alternateDigitSum(886996))