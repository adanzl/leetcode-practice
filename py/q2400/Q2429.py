"""
 * 给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：
 * 1、x 的置位数和 num2 相同，且
 * 2、x XOR num1 的值 最小
 * 注意 XOR 是按位异或运算。
 * 返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。
 * 整数的 置位数 是其二进制表示中 1 的数目。
 * 提示：1 <= num1, num2 <= 10^9
 * 链接：https://leetcode.cn/problems/minimize-xor/
"""


class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:
        b1, b2 = num1.bit_count(), num2.bit_count()
        ans = num1
        while b1 > b2:  # reduce last 1-0
            ans &= (ans - 1)
            b2 += 1
        while b1 < b2:  # add 0-1
            ans |= (ans + 1)
            b1 += 1
        return ans


if __name__ == '__main__':
    # 24
    print(Solution().minimizeXor(25, 72))
    # 3
    print(Solution().minimizeXor(3, 5))
    # 3
    print(Solution().minimizeXor(1, 12))
